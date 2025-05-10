from pathlib import Path
from PySide6.QtCore import QTimer, QThread, Signal, QObject, QPoint, Qt
from PySide6.QtWidgets import QApplication
import numpy as np
import time
import torch
import cv2
import time
from pathlib import Path
import os
import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized, TracedModel


configs = {'weights': 'yolov7.pt', 'source': 'data/coco/images/test',
               'img_size': 640, 'conf_thres': 0.25, 'iou_thres': 0.45,
               'device': '', 'view_img': False, 'save_txt': False,
               'save_conf': False, 'nosave': False, 'classes': None,
               'agnostic_nms': False, 'augment': False, 'update': False,
               'project': 'runs/detect', 'name': 'exp', 'exist_ok': False,
               'no_trace': False}
class YoloPredictor(QObject):

    yolo2main_pre_img = Signal(np.ndarray)  # raw image signal
    yolo2main_res_img = Signal(np.ndarray)  # test result signal
    yolo2main_status_msg = Signal(str)  # Detecting/pausing/stopping/testing complete/error reporting signal
    yolo2main_fps = Signal(str)  # fps
    yolo2main_labels = Signal(dict)  # Detected target results (number of each category)
    yolo2main_progress = Signal(int)  # Completeness
    yolo2main_class_num = Signal(int)  # Number of categories detected
    yolo2main_target_num = Signal(int)  # Targets detected

    def __init__(self):
        super().__init__()
        self.stop_detect = False


    # main for detect

    def detect(self,configs):
        source, weights, view_img, save_txt, imgsz, trace = configs['source'], configs['weights'], configs['view_img'], \
        configs['save_txt'], configs['img_size'], not configs['no_trace']
        delay = configs['delay']
        save_img = not configs['nosave'] and not source.endswith('.txt')  # save inference images
        webcam = source.isnumeric() or source.endswith('.txt') or source.lower().startswith(
            ('rtsp://', 'rtmp://', 'http://', 'https://'))

        # Directories

        save_dir = Path(
            increment_path(Path(configs['project']) / configs['name'], exist_ok=configs['exist_ok']))  # increment run
        (save_dir / 'labels' if save_txt else save_dir).mkdir(parents=True, exist_ok=True)  # make dir

        self.yolo2main_status_msg.emit('loading model')
        # QApplication.processEvents()
        # Initialize
        set_logging()
        device = select_device(configs['device'])
        half = device.type != 'cpu'  # half precision only supported on CUDA

        # Load model
        model = attempt_load(weights, map_location=device)  # load FP32 model
        stride = int(model.stride.max())  # model stride
        imgsz = check_img_size(imgsz, s=stride)  # check img_size

        if trace:
            model = TracedModel(model, device, configs['img_size'])

        if half:
            model.half()  # to FP16

        # Set Dataloader
        vid_path, vid_writer = None, None
        if webcam:
            view_img = check_imshow()
            cudnn.benchmark = True  # set True to speed up constant image size inference
            dataset = LoadStreams(source, img_size=imgsz, stride=stride)
        else:
            dataset = LoadImages(source, img_size=imgsz, stride=stride)

        # Get names and colors
        names = model.module.names if hasattr(model, 'module') else model.names
        colors = [[random.randint(0, 255) for _ in range(3)] for _ in names]

        # Run inference
        if device.type != 'cpu':
            model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))  # run once
        old_img_w = old_img_h = imgsz
        old_img_b = 1

        t0 = time.time()
        count = 1
        fps = str(0)

        if  os.path.isdir(source) == True:
            num = len(dataset)
        else:
            num = 0
        for id,(path, img, im0s, vid_cap) in enumerate(dataset):

            img = torch.from_numpy(img).to(device)
            img = img.half() if half else img.float()  # uint8 to fp16/32
            img /= 255.0  # 0 - 255 to 0.0 - 1.0
            if img.ndimension() == 3:
                img = img.unsqueeze(0)

            # Warmup
            if device.type != 'cpu' and (
                    old_img_b != img.shape[0] or old_img_h != img.shape[2] or old_img_w != img.shape[3]):
                old_img_b = img.shape[0]
                old_img_h = img.shape[2]
                old_img_w = img.shape[3]
                for i in range(3):
                    model(img, augment=configs['augment'])[0]

            # Inference
            t1 = time_synchronized()
            with torch.no_grad():  # Calculating gradients would cause a GPU memory leak
                pred = model(img, augment=configs['augment'])[0]
            t2 = time_synchronized()

            # Apply NMS
            pred = non_max_suppression(pred, configs['conf_thres'], configs['iou_thres'], classes=configs['classes'],
                                       agnostic=configs['agnostic_nms'])
            t3 = time_synchronized()

            if count%5 == 1:
                t_start = t1
            if count%5 == 0:
                t_end = time_synchronized()
                fps = str(int(5/(t_end-t_start)))
            count += 1

            self.yolo2main_fps.emit(fps)
            self.yolo2main_status_msg.emit('decting.....')

            total_boxes = 0
            unique_classes = set()
            # Process detections
            for i, det in enumerate(pred):  # detections per image
                if webcam:  # batch_size >= 1
                    p, s, im0, frame = path[i], '%g: ' % i, im0s[i].copy(), dataset.count
                else:
                    p, s, im0, frame = path, '', im0s, getattr(dataset, 'frame', 0)
                pre_img = im0.copy()
                p = Path(p)  # to Path
                save_path = str(save_dir / p.name)  # img.jpg
                txt_path = str(save_dir / 'labels' / p.stem) + (
                    '' if dataset.mode == 'image' else f'_{frame}')  # img.txt
                gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
                if len(det):

                    total_boxes += len(det)
                    unique_classes.update(det[:, -1].cpu().numpy())

                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                    # Print results
                    for c in det[:, -1].unique():
                        n = (det[:, -1] == c).sum()  # detections per class
                        s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                    # Write results
                    for *xyxy, conf, cls in reversed(det):
                        if save_txt:  # Write to file
                            xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                            line = (cls, *xywh, conf) if configs['save_conf'] else (cls, *xywh)  # label format
                            with open(txt_path + '.txt', 'a') as f:
                                f.write(('%g ' * len(line)).rstrip() % line + '\n')

                        if save_img or view_img:  # Add bbox to image
                            label = f'{names[int(cls)]} {conf:.2f}'
                            plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=1)

                self.yolo2main_class_num.emit(len(unique_classes))
                self.yolo2main_target_num.emit(total_boxes)
                self.yolo2main_pre_img.emit(pre_img)
                self.yolo2main_res_img.emit(im0)
                if  num != 0:
                    self.yolo2main_progress.emit(int(id/len(dataset)*100))

                if delay/1000>(1/(int(fps)+1e-10)):
                    time.sleep(delay/1000-(1/(int(fps)+1e-10)))
                    QApplication.processEvents()

                # Print time (inference + NMS)
                print(f'{s}Done. ({(1E3 * (t2 - t1)):.1f}ms) Inference, ({(1E3 * (t3 - t2)):.1f}ms) NMS')


                # Save results (image with detections)
                if save_img:
                    if dataset.mode == 'image':
                        cv2.imwrite(save_path, im0)
                        print(f" The image with the result is saved in: {save_path}")
                    else:  # 'video' or 'stream'
                        if vid_path != save_path:  # new video
                            vid_path = save_path
                            if isinstance(vid_writer, cv2.VideoWriter):
                                vid_writer.release()  # release previous video writer
                            if vid_cap:  # video
                                fps = vid_cap.get(cv2.CAP_PROP_FPS)
                                w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                                h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                            else:  # stream
                                fps, w, h = 30, im0.shape[1], im0.shape[0]
                                save_path += '.mp4'
                            vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
                        vid_writer.write(im0)


        if save_txt or save_img:
            s = f"\n{len(list(save_dir.glob('labels/*.txt')))} labels saved to {save_dir / 'labels'}" if save_txt else ''
            # print(f"Results saved to {save_dir}{s}")

        print(f'Done. ({time.time() - t0:.3f}s)')