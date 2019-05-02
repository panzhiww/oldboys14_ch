# time
# 计算时间差
# 坐时间格式的转换


# re模块
# 正则表达式

# 所有的模块要经历的两个步骤
    # 要操作的概念本身
    # 使用模块去操作它


# 学习    正则表达式   本身
    # 什么是正则表达式
        # 一种匹配字符串的规则
        # input 一串数据:
            # 是不是QQ号码: 全数字 5位以上   12位以下   第一位不是0
            # 是不是身份证号: 18位/15位  第一位不是0  18位的最后一位可能是X或者数字
        # 有一个文件
            # 要你把这个文件中所有的手机号摘取出来

    # 正则表达式能做什么
        # 可以定制一个规则,
            # 1. 来确认某一个字符串是否符合规则
            # 2. 从大段的字符串中找到符合规则的内容
        # 程序领域
            # 1. 登陆注册页的表单验证   web开发 要求简单
            # 2. 爬虫
                # 爬虫: 把这个网页下载下来   从里面提取一些信息, 找到我要的所有信息, 做数据分析
            # 3. 自动化开发
                # 日志开发

# 什么是正则表达式
    # 一种匹配字符串的规则.


# 明确一件事
    # 正则表达式是一种独立的语法
    # 和Python没关系

# 要先学习正则的语法
# 再学习使用Python来操作正则

# 帮助学习的工具
    # http://tool.chinaz.com/regex/



# 字符组 []    [^] |   ()
    # 在一个字符的位置上能够出现哪些内容
    # [1bc]   # 是一个范围
    # [0-9] [a-z]   [A-Z]   # 匹配三个字符
    # [0-9a-zA-Z]   # 匹配一个字符
    # [abc0-9]      # 匹配一个字符

# 18位身份证号码
# [1-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9x]

# \d == [0-9] 也表示匹配一个字符, 匹配的是一个数字   digit
# \w == [0-9a-zA-Z] 也表示匹配一个数字/字母/下划线, 匹配的是一个数字  word
# \s == [\n   \t]  表示匹配所有的空白符  回车/空格/制表符tab     space
    # \n 匹配回车
    # \t 匹配制表符
# \D  匹配非数字
# \Ｗ 匹配非制表符
# \S  匹配非空白

# [\d\D]    [\w\W]  [\s\S]    表示匹配所有

# 我写了一个规则是一个完整的规则, 不能岔开看
# 从头开始去匹配一个字符串
# 能匹配到多个符合规则的就是多条结果

# | 或: 两边规则要是有重合, 长的一部分要放在|左侧, 短的放在|"右侧

# ^ 匹配一个单词的开始
# $ 匹配一个单词的结束.

# [^XXXX]   匹配字符组中除了XXX的所有字符
# ()    匹配括号内的表达式，也表示一个组

# . 点是除了匹配换行符之外的任何结果