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
age = float(input('请输入你家狗狗年龄:'))
if age > 2:
    num = (age-2)*4 + 10.5*2
elif age <= 2:
    num =age * 10.5
print('这个狗狗相当于人类:',num,'岁')