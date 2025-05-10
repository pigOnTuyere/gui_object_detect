import sys
import os
import platform
import cv2
import argparse
from modules import *
from widgets import *
from predict import  YoloPredictor
from PySide6.QtGui import QAction
from PySide6.QtCore import QTimer, QThread, Signal
import yaml
from types import SimpleNamespace
from MangeData import read_json,update_data,write_json

# os.environ["QT_FONT_DPI"] = "150" # 修复高 DPI 和比例大于 100% 的问题

# Set as a global component
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    main2yolo_begin_sgl = Signal()
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # Use a custom title bar | For Mac or Linux, set it to "False"
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # set app name
        # ///////////////////////////////////////////////////////////////
        title = "Steel plate defect detection system"
        description = "Steel plate defect detection system"
        # apply name
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # Switch menu
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # 设置 UI 定义
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget parameters
        # ///////////////////////////////////////////////////////////////
        #widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 按钮点击
        # ///////////////////////////////////////////////////////////////

        # left menu
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets_train.clicked.connect(self.buttonClick)
        widgets.btn_imgs.clicked.connect(self.buttonClick)
        widgets.btn_video.clicked.connect(self.buttonClick)

        # set main parameters
        self.program_message = read_json('programMessage.json')
        print(self.program_message)
        widgets.pushButton_start.clicked.connect(self.buttonClick)


        self.configs = {'weights': 'best.pt', 'source': 'data/coco/images/test',
                   'img_size': 640, 'conf_thres': 0.25, 'iou_thres': 0.45,
                   'device': '', 'view_img': False, 'save_txt': False,
                   'save_conf': False, 'nosave': False, 'classes': None,
                   'agnostic_nms': False, 'augment': False, 'update': False,
                   'project': 'runs/detect', 'name': 'exp', 'exist_ok': False,
                   'no_trace': False,'delay':0}

        # Parameter binding

        # 1. 右侧参数设置
        widgets.horizontalSlider_conf.valueChanged.connect(lambda x: self.change_value(x, 'horizontalSlider_conf'))
        widgets.spinBox_conf.valueChanged.connect(lambda x: self.change_value(x, 'spinBox_conf'))
        widgets.horizontalSlider_iou.valueChanged.connect(lambda x: self.change_value(x, 'horizontalSlider_iou'))
        widgets.spinBox_iou.valueChanged.connect(lambda x: self.change_value(x, 'spinBox_iou'))
        # 2. 训练参数设置
        widgets.horizontalSlider_batchsize.valueChanged.connect(lambda x: self.change_value(x, 'horizontalSlider_batchsize'))
        widgets.spinBox_batchsize.valueChanged.connect(lambda x: self.change_value(x, 'spinBox_batchsize'))
        widgets.horizontalSlider_epoch.valueChanged.connect( lambda x: self.change_value(x, 'horizontalSlider_epoch'))
        widgets.spinBox_epoch.valueChanged.connect( lambda x: self.change_value(x, 'spinBox_epoch'))
        # 3. 检测主页面参数设置
        widgets.spinBox_delay.valueChanged.connect(lambda x: self.set_config('delay',x))

        # 按键绑定
        widgets.btn_imgs.clicked.connect(lambda x: self.openFolderDialog(flag="btn_imgs"))
        widgets.btn_video.clicked.connect(lambda x: self.openFolderDialog(flag="btn_video"))
        widgets.btn_camera.clicked.connect(lambda x: self.openFolderDialog(flag="btn_camera"))
        widgets.pushButton_data.clicked.connect(lambda x: self.openFolderDialog(flag="pushButton_data"))
        widgets.pushButton_hyp.clicked.connect(lambda x: self.openFolderDialog(flag="pushButton_hyp"))
        widgets.pushButton_weights.clicked.connect(lambda x: self.openFolderDialog(flag="pushButton_weights"))
        widgets.closeAppBtn.clicked.connect(lambda x: self.openFolderDialog(flag="closeAppBtn"))
        widgets.pushButton_hyp.clicked.connect(lambda x: self.openFolderDialog(flag = 'pushButton_hyp'))
        widgets.pushButton_thyp.clicked.connect(lambda x: self.openFolderDialog(flag = 'pushButton_thyp'))

        # YOLOv7
        self.yolo_predict = YoloPredictor()
        self.yolo_thread = QThread()
        self.yolo_predict.yolo2main_pre_img.connect(lambda x: self.show_image(x, widgets.label_video))
        self.yolo_predict.yolo2main_res_img.connect(lambda x: self.show_image(x, widgets.label_result))
        self.yolo_predict.yolo2main_status_msg.connect(lambda x: widgets.label_status.setText(str(x)))
        self.yolo_predict.yolo2main_class_num.connect(lambda x: widgets.label_classes.setText(str(x)))
        self.yolo_predict.yolo2main_target_num.connect(lambda x: widgets.label_targets.setText(str(x)))
        widgets.progressBar.hide()
        self.yolo_predict.yolo2main_progress.connect(lambda x: self.bar_progress_show(x))
        self.yolo_predict.yolo2main_fps.connect(lambda x: widgets.label_FPS.setText(str(x)))
        self.main2yolo_begin_sgl.connect(self.yolo_predict.detect)
        self.yolo_predict.moveToThread(self.yolo_thread)

        # 窗口图片展示
        widgets.pushButton_start.clicked.connect(lambda: self.yolo_predict.detect(self.configs))

        # 设置隐藏菜单栏

        self.load_model = QAction('load a new model')


        self.ui.btn_imgs.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.btn_imgs.customContextMenuRequested.connect(lambda pos: self.showContextMenu(self.ui.btn_imgs, pos, "images_folder"))

        self.ui.btn_video.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.btn_video.customContextMenuRequested.connect(lambda pos: self.showContextMenu(self.ui.btn_video, pos, "video_folder"))

        self.ui.btn_camera.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.btn_camera.customContextMenuRequested.connect(lambda pos: self.showContextMenu(self.ui.btn_camera, pos, "btn_camera"))
        
        

        self.ui.comboBox_select_model.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.ui.comboBox_select_model.addAction(self.load_model)




        # self.show_image(img,widgets.label_result)

        # 额外的左框
        # def openCloseLeftBox():
        #     UIFunctions.toggleLeftBox(self, True)
        # widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        # widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # 额外的右框
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # 显示应用程序
        # ///////////////////////////////////////////////////////////////
        self.show()

        # 设置自定义主题
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # 设置主题和修补程序
        if useCustomTheme:
            # 加载和应用样式
            UIFunctions.theme(self, themeFile, True)

            # 设置修补程序
            AppFunctions.setThemeHack(self)

        # 设置主页并选择菜单
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def showContextMenu(self,button, position,menu_type):

        context_menu = QMenu(button)
        if menu_type == "images_folder" or menu_type == "video_folder" :
            # 添加固定动作
            open_action = QAction('Open Folder', self)
    
            # 连接动作信号
            # open_action.triggered.connect(self.openFolder)
            # 添加动作到菜单
            context_menu.addAction(open_action)
            # 创建一个子菜单用来显示路径
            file_menu = QMenu("Recent Folder", self)
            file_menu.setStyleSheet("""QMenu {
                                   background-color: rgba(50, 50, 50, 180); /* 半透明灰黑色背景 */
                                   color: white; 
                                   border: 1px solid #333;
                               }""")
            try:
                if self.program_message[menu_type] != None:
                    for path in self.program_message[menu_type]:
                   
                        path_action = QAction(path, self)
                        file_menu.addAction(path_action)

            except Exception as e:
                pass
            context_menu.addMenu(file_menu)

        elif menu_type == "btn_camera":
            # camreas  = self.check_available_cameras()
            # View 菜单项
            context_menu.addAction(QAction("camera 0", self))
            context_menu.addAction(QAction("camera 1", self))

        # 显示菜单
        context_menu.exec(button.mapToGlobal(position))

    def check_available_cameras(self,limit=10):
        available_cameras = []
        # 尝试从索引 0 到 limit 检查可用的摄像头
        for index in range(limit):
            cap = cv2.VideoCapture(index)
            if cap.isOpened():  # 如果能打开摄像头，说明是有效的
                available_cameras.append(index)
                cap.release()  # 不要忘记释放资源
        return available_cameras
    def set_config(self,key, value):
        self.configs[key] = value
    def bar_progress_show(self,x):
        self.ui.progressBar.show()
        self.ui.progressBar.setValue(x)
    def extralRigtBox(self):
        btn = self.sender()
        btnName = btn.objectName()
        print(btnName)

    def change_value(self, x, flag):
        if flag == 'spinBox_iou':
            # print(x)
            widgets.horizontalSlider_iou.setValue(int(x))  # The box value changes, changing the slider
        elif flag == 'horizontalSlider_iou':
            widgets.spinBox_iou.setValue(int(x))  # The slider value changes, changing the box
            self.configs['iou_thres'] = int(x)/100.

            # self.show_status('IOU Threshold: %s' % str(x / 100))
            # self.yolo_predict.iou_thres = x / 100
        elif flag == 'spinBox_conf':
            widgets.horizontalSlider_conf.setValue(int(x))
        elif flag == 'horizontalSlider_conf':
            widgets.spinBox_conf.setValue(int(x))
            self.configs['conf_thres'] = int(x) / 100.
        elif flag == 'horizontalSlider_batchsize':
            widgets.spinBox_batchsize.setValue(int(x))
        elif flag == 'spinBox_batchsize':
            widgets.horizontalSlider_batchsize.setValue(int(x))
        elif flag == 'horizontalSlider_epoch':
            widgets.spinBox_epoch.setValue(int(x))
        elif flag == 'spinBox_epoch':
            widgets.horizontalSlider_epoch.setValue(int(x))

    def openFolderDialog(self,flag):
        # 打开文件夹选择对话框

        if flag == 'pushButton_data':
            folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
            self.ui.lineEdit_data.setText(folder_path)
        elif flag == 'pushButton_weights':
            file_path, _ = QFileDialog.getOpenFileName(self, "Select .pt")
            self.ui.lineEdit_weights.setText(file_path)
        elif flag == "btn_imgs":
            folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
            if folder_path !=None:
                self.ui.lineEdit_mode.setText(folder_path)

                images_folders = set(self.program_message["images_folder"])
                images_folders.add(folder_path)
                self.program_message["images_folder"] = list(images_folders)
        elif flag == 'btn_video':
            file_path, _ = QFileDialog.getOpenFileName(self, "Select .mp4,")
            self.ui.lineEdit_mode.setText(file_path)
            self.configs['source'] = file_path
        elif flag == 'btn_camera':
             self.configs['source'] = '0'
             self.ui.lineEdit_mode.setText('camera 0')
        elif flag == 'closeAppBtn':
            update_data('programMessage.json',self.program_message)
            cv2.destroyAllWindows()
            sys.exit()
        elif flag == 'pushButton_hyp':
            file_path, _ = QFileDialog.getOpenFileName(self, "Select .yaml")
            try:
                # 打开并读取 YAML 文件
                with open(file_path, 'r') as file:
                    data = yaml.safe_load(file)  # 使用 safe_load 来读取文件
                # 将 YAML 数据转换为字符串并显示在 plainTextEdit 中
                self.ui.lineEdit_hyp.setText(file_path)
                self.ui.plainTextEdit_yaml.setPlainText(yaml.dump(data, sort_keys=False, allow_unicode=True))
            except Exception as e:
                # 如果出错，显示错误信息
                self.ui.plainTextEdit_yaml.setPlainText(f"Error reading YAML file: {str(e)}")
            # 这里可以保存或处理 folder_path
        elif flag  == 'pushButton_thyp':
            file_path, _ = QFileDialog.getOpenFileName(self, "Select .yaml")
            try:
                # 打开并读取 YAML 文件
                with open(file_path, 'r') as file:
                    data = yaml.safe_load(file)  # 使用 safe_load 来读取文件
                # 将 YAML 数据转换为字符串并显示在 plainTextEdit 中
                self.ui.lineEdit_thyp.setText(file_path)
                self.ui.plainTextEdit_yaml.setPlainText(yaml.dump(data, sort_keys=False, allow_unicode=True))

                self.opt = SimpleNamespace(**data)


            except Exception as e:
                # 如果出错，显示错误信息
                self.ui.plainTextEdit_yaml.setPlainText(f"Error reading YAML file: {str(e)}")

    def dict_to_argparse_options(self, args_dict):
        # 创建 ArgumentParser 对象
        parser = argparse.ArgumentParser(description="Parse dictionary arguments")

        # 根据字典中的键值对添加参数
        for key, value in args_dict.items():
            parser.add_argument(f'--{key}')

        # 模拟命令行输入
        simulated_args = []
        for key, value in args_dict.items():
            simulated_args.extend([f'--{key}', value])

        # 解析参数
        opts = parser.parse_args(simulated_args)
        return opts

    # 按钮点击
    # 在这里添加单击按钮的功能
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # 获取点击的按钮
        btn = self.sender()
        btnName = btn.objectName()

        # 显示主页
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # 显示小部件页
        if btnName == "btn_widgets_train":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # 显示新页面
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page)  # 设置页面
            UIFunctions.resetStyle(self, btnName)  # 重置其他按钮的选择
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # 选择菜单

        if btnName == "btn_save":
            print("保存按钮被点击！")

        if btnName == 'pushButton_start':
            name = widgets.pushButton_start.text()
            if name == 'start':
                widgets.pushButton_start.setText('stop')

            else:
                widgets.pushButton_start.setText('start')


        # 打印按钮名称
        print(f'按钮 "{btnName}" 被按下！')


    # 调整大小事件
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # 更新大小调整手柄
        UIFunctions.resize_grips(self)

    # 鼠标单击事件
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # 设置拖动位置
        self.dragPos = event.globalPos()

        # 打印鼠标事件
        if event.buttons() == Qt.LeftButton:
            print('鼠标点击: 左键单击')
        if event.buttons() == Qt.RightButton:
            print('鼠标点击: 右键单击')

    def run_or_continue(self):
        # if self.yolo_predict.source == '':
        #     self.show_status('Please select a video source before starting detection...')
        #     self.run_button.setChecked(False)
        if self.yolo_predict.stop_detect == False:
            if self.ui.pushButton_start.isChecked():
                self.run_button.setChecked(True)    # start button
                self.save_txt_button.setEnabled(False)  # It is forbidden to check and save after starting the detection
                self.save_res_button.setEnabled(False)
                self.show_status('Detecting...')
                self.yolo_predict.continue_dtc = True   # Control whether Yolo is paused

        if not self.yolo_thread.isRunning():
                self.yolo_thread.start()
                self.main2yolo_begin_sgl.emit(self.configs)
            # else:
            #     self.yolo_predict.continue_dtc = False
            #     self.show_status("Pause...")
            #     self.run_button.setChecked(False)

    @staticmethod
    def show_image(img_src, label):
        try:
            ih, iw, _ = img_src.shape
            w = label.geometry().width()-10
            h = label.geometry().height()-10

            # keep the original data ratio
            if iw/w > ih/h:
                scal = w / iw
                nw = w
                nh = int(scal * ih)
                img_src_ = cv2.resize(img_src, (nw, nh))

            else:
                scal = h / ih
                nw = int(scal * iw)
                nh = h
                img_src_ = cv2.resize(img_src, (nw, nh))

            frame = cv2.cvtColor(img_src_, cv2.COLOR_BGR2RGB)
            img = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[2] * frame.shape[1],
                         QImage.Format_RGB888)
            label.setPixmap(QPixmap.fromImage(img))

        except Exception as e:
            print(repr(e))



    def show_status(self, msg):
        self.ui.label_status.setText(msg)
        if msg == 'Detection completed' or msg == '检测完成':
            pass
            # self.save_res_button.setEnabled(True)
            # self.save_txt_button.setEnabled(True)
            # self.run_button.setChecked(False)
            # self.progress_bar.setValue(0)
            # if self.yolo_thread.isRunning():
            #     self.yolo_thread.quit()         # end process
        elif msg == 'Detection terminated!' or msg == '检测终止':
            pass
            # self.save_res_button.setEnabled(True)
            # self.save_txt_button.setEnabled(True)
            # self.run_button.setChecked(False)
            # self.progress_bar.setValue(0)
            # if self.yolo_thread.isRunning():
            #     self.yolo_thread.quit()         # end process
            # self.pre_video.clear()           # clear image display
            # self.res_video.clear()
            # self.Class_num.setText('--')
            # self.Target_num.setText('--')
            # self.fps_label.setText('--')
    def load_configs(self):

        if self.ui.spinBox_conf.value() != 0:
            self.configs['conf_thres'] = self.ui.spinBox_conf.value()/100
            # print('spinBox_conf',self.ui.spinBox_conf.value()/100)

        if  self.ui.spinBox_iou != 0:
            self.configs['iou_thres']  = self.ui.spinBox_iou.value()
            # print('spinBox_iou',self.ui.spinBox_iou.value() / 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("defectDetect.svg"))
    window = MainWindow()
    sys.exit(app.exec())
