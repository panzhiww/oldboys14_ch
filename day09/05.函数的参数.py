# def yue(fangshi):   # 形参
#     print("打开手机")
#     print("打开%s" % fangshi)
#     print("找一个漂亮的妹子")
#     print("出来约一约")
#
#
# yue("探探")   # 实参
# yue("陌陌")

# 参数: 在函数执行的时候给函数传递的信息
# 形参: 在函数声明的位置, 声明出来的变量
# 实参: 在函数调用的时候, 实际你给函数传递的值
# 函数的参数个数是没有要求是的    但是, 在运行的时候, 形参和实参都要匹配,按照位置把实参赋值给形参

# 参数的分类:
#   站在实参的角度:    在函数调用的时候, 给函数传递的具体的值
#       1. 位置参数
#       2. 关键字参数
#       3. 混合参数, 注意顺序. 先写位置参数, 然后写关键字参数, 否则会报错
#   站在形参的角度:    在函数声明的位置
#       1. 位置参数
#       2. 默认值参数
#       3. 默认值参数和位置参数混合使用. 顺序: 先写位置参数, 然后再写默认值参数


# def yue(fangshi,age):
#     print("打开手机")
#     print("打开%s" % fangshi)
#     print("找一个漂亮的妹子")
#     print("年龄最好是%s" % age)
#     print("出来约一约")
#
#
# yue("探探",38)
# yue("陌陌",26)


# def gn(name,age,address,id,sex,hobby):
#     print("人的名字叫%s,年龄:%s,地址:%s,id是:%s,性别:%s,爱好是:%s" % (name,age,address,id,sex,hobby))
# gn("太白",58,"保定",1,"不详","女")     # 位置参数
# gn(id = 1, name = "太白", address = "保定", hobby = "女", age = 58, sex = "不详")    # 关键字参数
# gn("太白",58,"保定",id="3",sex="不详",hobby="女")      # 混合参数


def regist(id,name,sex="男"):
    print("录入学生信息:id是%s,名字是%s,性别是%s" % (id,name,sex))

regist(1,"大阳哥")
regist(1,"徐卫星")
regist(1,"毛建妹妹","女")


