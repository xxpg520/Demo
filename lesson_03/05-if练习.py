# 练习1:
#   编写一个程序,获取一个用户输入的整数.然后通过程序显示i这个数时奇数还是偶数
# 获取用户输入的整数
# num = int(input('请输入一个任意的整数:'))
#
# # 显示num时奇数还是偶数
# if num % 2 == 0 :
#     print(num,'是偶数')
# else :
#     print(num,'是奇数')

# 练习2:
#   编写一个程序,检查任意一个年份是否是闰年.
#   如果一个年份可以被4整除不能被100整除,或者可以被400整除,这个年份就是闰年

# year = int(input('请输入一个任意年份:'))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
#     print(year,'是闰年')
# else :
#     print(year,'是平年')

# 练习3:
#   我家的狗5岁了,5月的狗相当于多大年龄的人呢?
#   其实非常简单,狗的前两年每一年相当于人类的10.5岁,然后每增加一年就增加4岁.
#   那么5岁的狗相当于人类年龄就应该是10.5+10.5+4+4+4 = 33岁

#   编写一个程序,获取用户输入的狗的年龄,然后通过程序显示其相当于人类的年龄.
#   如果用户输入负数,请显示一个提示信息
# dog_age = float(input('请输入你家狗狗年龄:'))
# like_person_age = 0
# 检查用户输入的是否是负数
# if dog_age < 0:
#     print('你输入的不合法！')
# # 如果狗的年龄在两岁以上
# elif dog_age > 2:
#     # 计算前两岁相当于人类的年纪
#     like_person_age = 2 * 10.5
#     # 计算超过两岁的部分相当于人类的年纪，并进行相加
#     like_person_age += (dog_age - 2) * 4
# # 如果狗的年龄在两岁一下（包含两岁）
# elif dog_age <= 2:
#     # 直接将当前的年龄乘以10.5
#     like_person_age =dog_age * 10.5
# if dog_age > 0 :
#     print(dog_age,'岁狗狗相当于人类:',like_person_age,'岁')

# 在if也可以去嵌套if，代码块是可以嵌套的，每增加一个缩进的级别，代码块就低一级
# 检查用户的输入是否合法
# if dog_age > 0:
#     # 如果狗的年龄在两岁以上
#     if dog_age > 2:
#         # 计算前两岁相当于人类的年纪
#         like_person_age = 2 * 10.5
#         # 计算超过两岁的部分相当于人类的年纪，并进行相加
#         like_person_age += (dog_age - 2) * 4
#     # 如果狗的年龄在两岁一下（包含两岁）
#     else:
#         # 直接将当前的年龄乘以10.5
#         like_person_age =dog_age * 10.5
#     print(dog_age,'岁狗狗相当于人类:',like_person_age,'岁')
# else:
#     print('你输入的数据不合法！')


# 练习4：
#   从键盘输入小明的期末成绩：
#       当成绩为100时，’奖励一辆BMW'
#       当成绩为[80-99]，‘奖励一台iphone’
#       当成绩为[60-79]，‘奖励一本参考书’
#       其他时，什么奖励也没有

# numb = float(input('请输入考试成绩:(0~100)'))
# print('=' * 40) #增加一行分隔符
# #  检查用户的输入是否合法
# if 0 <= numb <= 100 :
#     if numb == 100:
#         print('考得好，奖励一台BMW')
#     elif 99 > numb >= 80 :
#         print('还不错，奖励一台iphone')
#     elif 79 > numb >= 60 :
#         print('考的一般，奖励一本参考书，下次加油')
#     else:
#         print('考的太差，挨揍！')
# else:
#     # 用户输入的不合法，弹出一个友好提示
#     print('请输入正确成绩！')

# 练习5：
#   大家都知道，男大当婚，女大当嫁。那么女方家长要嫁女儿，当然要提出一定的条件：
#       高:180cm以上; 富:1000万以上;帅:500以上;
#       如果这三个条件同时满足,则:'我一定要嫁给他'
#       如果三个条件有为真的情况,则:'嫁吧,比上不足,比下有余.'
#       如果三个条件都不满足,则:'不嫁!'

height = float(input('请输入身高(单位:cm):')) #获取身高数值
money = float(input('请输入资产(单位:万)')) #获取资产数值
face = float(input('请输入颜值分数'))  #获取颜值分数
print('=' * 40)  #分隔符
# 判断身高>180 并且 资产>1000万并且 颜值500分以上
if height > 180 and money > 1000 and face > 500:
    print('我一定要嫁给他')
# 判断身高/资产/颜值中有一条符合要求
elif height > 180 or money > 1000 or face > 500:
    print('嫁吧,比上不足,比下有余.')
# 以上条件都不满足
else:
    print('不嫁')