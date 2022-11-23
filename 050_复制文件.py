# 1.获取待操作文件
old_file_name = input('输入待操作文件名：')
# 2.生成待操作文件名
old_file = open(old_file_name, 'r')
# 3.新建文件
new_file = open('复制文件（副本）.txt', 'w')
# 4.复制内容
content = old_file.read()
new_file.write(content)
# 5.关闭文件
old_file.close()
new_file.close()
