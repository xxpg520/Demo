
# 循环语句
# 循环语句可以使指定的代码快重复指定的次数
# 循环语句分成两种,while循环和for循环
# while循环
# 语法:
#   while 条件表达式:
#       代码块
# 执行流程:
#   while语句在执行时,会先对while后的条件表达式进行求值判断,
#       如果循环判断结果为True,则执行循环体(代码块),
#       循环体执行完毕,继续对条件表达式进行求值判断,以此类推,
#       知道判断结果为false,则循环终止,如果循环有对应的else,则执行else后的代码块

# 条件表达式恒为True的循环语句,称为死循环,它会一直运行,慎用!
# while True :
#     print('hello')
# 循环的三个要件(表达式)
# 初始化表达式,通过初始化表达式初始化一个变量
# i = 0
#
# # 条件表达式,条件表达式用来设置循环执行的条件
# while i < 10:
#     # 更新表达式
#     i += 1
#     print(i)

# 创建一个执行十次的循环
# i = 0
# while i < 10:
#     i += 1
#     print(i,'hello')
# else:
#     print('else中的代码块')

numb = 0
flag = 0
while numb < 100:
    flag += numb
    numb += 1

print(flag)






# 练习1:
#   求100以内所有的奇数之和
# numb = 0
# i = 0
# while i < 100 :
#     if i % 2 != 0 :
#         numb += i
#     i += 1
# print(numb)

# 获取100以内所有的奇数
# i = 1
# while i < 100 :
#     print(i)
#     i += 2

# 练习100以内所有7的倍数之和,以及个数
# numb = 0
# i = 1
# while i < 100 :
#     if i % 7 == 0:
#         numb += i
#     i += 1
# print(numb)