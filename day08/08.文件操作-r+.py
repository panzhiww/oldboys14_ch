# f = open("老师点名",mode="r+",encoding="utf-8")
# s = f.read()
# f.write("周杰伦")
# print(s)
# f.flush()
# f.close()


# f = open("老师点名",mode="r+",encoding="utf-8")     #  r+ 模式, 默认情况下光标在文件的开头, 必须先读, 后写
# f.write("周润发")
# s = f.read()
# print(s)
# f.flush()
# f.close()


# f = open("精品",mode="r+",encoding="utf-8")
# s = f.read(3)
# # ss = f.read(3)
# # print(ss)
# print(s)
# f.flush()
# f.close()


# f = open("精品",mode="r+",encoding="utf-8")
# s = f.read(3)
# #  不管你前面读了几个, 后面去写都是在末尾
# f.write("哈哈")   #  1. 在没有任何操作之前进行写. 在开头写    2. 如果读取了一些内容, 再写, 写入的是最后


f = open("精品",mode="r+",encoding="utf-8")
# f.seek(3)     #  byte 字节
# 移动到开头: f.seek(0)
# 移动到结尾: f.seek(0,2)

# 浓缩的都是精品,我就不是精品,潘长江的精品哈哈哈哈
# f.seek(6)    # 移动6个字节,2个字
# s = f.read(3)     #  读取3个字
# print(s)
# ss = f.read(3)
# print(ss)
# f.seek(0)
# sss = f.read(3)
# print(sss)

# s = f.read()
f.seek(6)
ss = f.read()
# print(s)
print(ss)
f.flush()
f.close()

