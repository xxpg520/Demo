# 练习1
#     打印99乘法表
#     1*1=1
#     1*2=2 2*2=4
#     1*3=3 2*3=6 3*3=9
#     …………


# 创建一个外层循环来控制图形的高度
i = 0
while i < 9:
    i += 1

    # 创建一个内层循环来控制图形的宽度
    j = 0
    while j < i:
        j += 1
        print(f'{j}*{i}={i * j}', end='       ')
    print()
