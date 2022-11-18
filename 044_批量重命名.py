import os

img_path = os.path.abspath("D:\PROGRAM\qqd\Download\images")
img_list = os.listdir(img_path)
i = 0
for img in img_list:
    i += 1
    if img.endswith('.bin'):
        print(i)
        old_file_name = img
        new_file_name = old_file_name[:old_file_name.rfind('.')]+".png"
        os.chdir(img_path)
        os.rename(old_file_name,new_file_name)