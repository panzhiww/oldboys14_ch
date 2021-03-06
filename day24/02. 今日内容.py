# 模块  *****
# 什么是模块
# 为什么要有模块
# 模块分为哪几种
# import
    # import 的时候发生了什么
    # 在import的时候命名空间的变换
    # 重命名
    # 一行导入多个模块
# from ... import ...
    # from import 的时候发生了什么
    # 在import的时候命名空间的变换
    # 重命名 as
    # 一行导入多个名字
    # from 模块 import *
    # * 和 __all__ 的相关性
# 模块相关的其他知识
    # 1.把模块当成脚本运行  : 从本模块中反射本模块中的变量
    # if __name__ == '__main__':
    #     所有不需要调用就能执行的内容
    # import sys
    # getattr(sys.modules[__name__],'要反射的变量名')
    # 2.模块搜索路径   sys.path
    # 3.pyc编译文件
    # 4.重新加载模块 已经导入的模块即便被修改在程序执行过程中也不会生效
    # 5.模块的循环引用 - 不允许
# 包 ***
# 什么是包? 集合了一组py文件 提供了一组复杂功能的
# 为什么要有包?  当提供的功能比较复杂,一个py文件写不下的时候
# 包中都有什么?  至少拥有一个__init__.py
# 直接导入模块
    # import 包.包.模块
    # 包.包.模块.变量
    # from 包.包 import 模块  # 推荐 平时写作业的过程
    # 模块.变量
# 导入包 读框架源码的时候
    # 如要希望导入包之后 模块能够正常的使用 那么需要自己去完成init文件的开发
    # 包中模块的 绝对导入
    # 包中模块的 相对导入
        # 使用了相对导入的模块只能被当做模块执行
        # 不能被当做脚本执行
