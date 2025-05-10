import json

# 文件名
filename = 'data.json'

# 读取 JSON 文件
def read_json(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# 写入 JSON 文件
def write_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# 更新数据
def update_data(filename, updates):
    data = read_json(filename)
    data.update(updates)
    write_json(data, filename)

# 初始数据
initial_data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "children": ["Jane Doe", "John Doe Jr."]
}

# 更新数据示例
updates = {
    "age": 31,  # 更新年龄
    "city": "Los Angeles",  # 更新城市
    "children": ["Jane Doe", "John Doe Jr.", "Jimmy Doe"]  # 更新子女信息
}

if __name__ == "__main__":
    # 写入初始数据
    write_json(initial_data, filename)
    # 应用更新
    update_data(filename, updates)

    # 读取并打印更新后的数据
    updated_data = read_json(filename)
    print(updated_data)
