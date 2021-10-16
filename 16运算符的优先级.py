a = 10
b = 20
c = 30

#  通过条件运算符获取三个值中的最大值
max = a if a > b else b
max = max if max >c else c

print(max)