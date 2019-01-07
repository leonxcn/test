# 1. 把 jpg,png,gif 文件夹中的所有文件移动到 image 文件夹中，然后删除 jpg,png,gif 文件夹
# 2. 把 doc,docx,md,ppt 文件夹中的所有文件移动到 document 文件夹中，然后删除
import os
import shutil

path = r'E:\OneDrive\Python\version last\problem2_files'
image_path = path + "\\" + "image"
doc_path = path + "\\" + "document"

img = ["jpg", "png", "gif"]
doc = ["doc", "docx", "md", "ppt"]

# 判断是否有文件夹，要是没有就建立
for i in [image_path, doc_path]:
    if not os.path.isdir(i):
        os.mkdir(i)

for i in img:
    current_path = os.path.join(path, i)
    for file in os.listdir(current_path):
        shutil.move(os.path.join(current_path, file), image_path)
    os.removedirs(current_path)

for i in doc:
    current_path = os.path.join(path, i)
    for file in os.listdir(current_path):
        shutil.move(os.path.join(current_path, file), doc_path)
    os.removedirs(current_path)
