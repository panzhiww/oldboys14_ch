# 正则表达式里的转义

# "\("  表示匹配小括号
# [()+*?/$.]     在字符组中一些特殊的字符会现出原形
# 所有的\w \d \s \n \t \W \D \S 都表是它原本的意义
# [-] 只有写在字符组收尾的时候表示普通的减号
    # 在写在其他位置的时候表示范围[1-9]
    # 如果就是想匹配减号[1\-9]







# Python中的转义符

# 分析过程
# "\n"    # \ 转义符  赋予这个n一个特殊的意义, 表示一个换行符
# print("\\n")
# print("C:\\next")
# print(r"C:\next")

# "\\\\n"   "\\n"
#结论
# r"\\n"    r"\n"   在Python中

