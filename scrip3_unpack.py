"""
监测 image 文件夹，如果包含的文件大于等于 5 个，则将这些文件压缩到 archive1.zip 文件中，
并删除这些文件。当再次监测到文件多于 5 个的时候，生成 archive2.zip 压缩包，以此类推。
图片素材压缩包：https://video.mugglecode.com/image.zip，请下载后解压使用

Tips： 
shutil 库中的 make_archive 函数可以生成压缩包，使用方法如下： 
make_archive(path1, 'zip', path2) 
其中 path1 是生成压缩包的路径（包含压缩包名称），path2是需要被压缩的文件夹。

"""
import os
import shutil
import time

# 示例里的解决方案有些缺陷
# 要解决需要加图片临时存放地点 img_path
path = r"E:\OneDrive\Python\version last\image"
img_path = r"E:\OneDrive\Python\version last\zip"
archive_path = r"E:\OneDrive\Python\version last\zip2"
count = 0

while True:
    if len(os.listdir(path)) >= 5:
        count = count + 1
        for file in os.listdir(path)[:5]:
            shutil.move(os.path.join(path, file), img_path)
            # 5张图片移动到临时图片文件夹
            # shutil.move(src, dst, copy_function=copy2)
            # Recursively move a file or directory (src) to another location (dst) and return the destination.
    zip_name = os.path.join(archive_path, "archive" + str(count))
    # 需要生成zip的path+name
    shutil.make_archive(zip_name, 'zip', img_path)
    # Create an archive file (such as zip or tar) and return its name.
    # base_name is the name of the file to create, including the path, minus any format-specific extension
    # root_dir and base_dir both default to the current directory
    # 这个函数第一个参数是，要生成zip的路径加名字
    # 第2个是格式zip, 第3个是需要压缩的目录
    for f in os.listdir(img_path):
        os.remove(os.path.join(img_path, f))
        # 删除临时文件夹下的图片
    time.sleep(10)
