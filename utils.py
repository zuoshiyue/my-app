import json
from pathlib import Path

def load_data(filename):
    file_path = Path(filename)
    try:
        # 检查文件是否存在且不为空
        if file_path.exists() and file_path.stat().st_size > 0:
            with open(file_path, 'r') as file:
                return json.load(file)
        else:
            print("文件不存在或为空，将返回空列表或创建新文件。")
            # 文件不存在或为空，可以选择返回空列表或创建一个空文件
            # return []
            # 或者创建一个空的JSON数组文件
            save_data([], filename)
    except json.JSONDecodeError as e:
        print(f"解析JSON时发生错误：{e}")
    except FileNotFoundError:
        print(f"未找到文件：{filename}")
    except Exception as e:
        print(f"读取文件时发生未预料的错误：{e}")

    # 如果有错误或文件不存在/为空，则返回空列表
    return []

def save_data(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"写入文件时发生错误：{e}")