import os
import re

list_all = []

# 文件夹下所有文件的文件名
for root, dirs, files in os.walk('D:\\file_test'):
    for name in files:
        file_path = os.path.join(root, name)

        # ('D:\\免安装软件\\v2rayN-Core', 'config.json')
        print(os.path.split(file_path))

        # 截取文件名
        file_name = os.path.split(file_path)[-1]
        list_all.append(file_name)

print(list_all)

# 文件重命名
# 匹配所有ppt文件，r加上能保证正则少出问题
pattern = re.compile(r'.+\.pptx')
for root, dirs, files in os.walk('D:\\file_test'):
    for name in files:
        file_path = os.path.join(root, name)
        matching = pattern.search(file_path)
        # 查看匹配到的
        # print(matching)
        if matching:
            os.rename(file_path, os.path.split(file_path)[-2] + '/123.pptx')

# 复制和删除文件
pattern = re.compile(r'.+\.pptx')
for root, dirs, files in os.walk('D:\\file_test'):
    for name in files:
        file_path = os.path.join(root, name)
        matching = pattern.search(file_path)
        if matching:
            # 相当于调用windows的命令行  file_test2文件夹要先创建好
            command_line = 'copy %s d:\\file_test2' % file_path.replace('/', '\\')
            os.system(command_line)
            # 删除原先目录下的文件
            os.remove(file_path)


