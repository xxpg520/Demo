# break
# break可以用来立即退出循环语句
# continue
# continue可以用来跳过档次循环

# 创建一个5次的循环
i = 0
while i < 5 :
    if i == 3:
        break
    print(i)
    i += 1
else:
    print('循环结束')