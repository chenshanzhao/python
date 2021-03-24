'''
Created on 2019年11月6日

@author: chensz
'''
import random

num = random.randint(1, 100)  # 随机产生的数字

for i in range(3):
    guess = int(input('请输入一个数'))
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