'''
Created on 2019年11月6日

@author: chensz
'''
import random

num = random.randint(1, 100)  # 随机产生的数字

count = 0
while count < 7:
    count += 1
    guess = int(input('请猜一个数：'))  # 转成int类型
    if guess > num:
        print('大了')
        continue
    elif guess == num:
        print('对了')
        break
    else:
        print('小了')
        continue
else:
    print('错误次数过多')
