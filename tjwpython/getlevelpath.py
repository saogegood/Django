"""
Module/Script Name:<getlevelpath>
Author: <Devin>
Date: <2023/4/2 11:38>
Description: <Description of Module/Script>
"""

import os


# 创建人：AI Chatbot
# 创建时间：2023年4月3日
# 描述：这个类用于探索指定路径下指定层数内的所有目录和文件的路径列表。

class FilesystemPathExplorer:
    def __init__(self, path):
        # 构造函数，接收一个路径参数并将其存储在类的属性中。
        self.path = path

    def get_all_paths_in_dir(self, level):
        # 获取指定路径下指定层数内的所有目录和文件的路径列表。
        # 用于存储所有路径的列表
        all_paths = []

        # 如果指定层数为0，则返回空列表
        if level == 0:
            return all_paths

        # 遍历指定路径下的所有项目
        for item in os.listdir(self.path):
            # 构造项目的完整路径
            item_path = os.path.join(self.path, item)

            # 如果是目录，则递归获取所有子目录中的路径
            if os.path.isdir(item_path):
                # 将当前目录的路径加入列表中
                all_paths.append(item_path)

                # 如果指定层数大于1，则递归获取子目录中的路径
                if level > 1:
                    sub_paths = FilesystemPathExplorer(item_path).get_all_paths_in_dir(level - 1)
                    all_paths.extend(sub_paths)

            # 如果是文件，则将文件的路径加入列表中
            else:
                all_paths.append(item_path)

        # 返回所有路径的列表
        return all_paths


# 示例使用
path = "D:"     #这里输入需要搜索的路径
level = 2       #这里输入需要返回路径的层数
explorer = FilesystemPathExplorer(path)
all_paths = explorer.get_all_paths_in_dir(level)
for item in all_paths:
    print(item)
