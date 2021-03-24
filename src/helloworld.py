'''
Created on 2019年11月6日

@author: chensz
'''
print("hello world");
print ("Hello, Python!");
'''
    测试循环判断
'''
#单行注释
if 1<0:
    print ("true")
else:
    print ("false")
    
if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
    # 没有严格缩进，在执行时会报错
    print ("False")
    
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
#if判断长度
if len(days)==1 : 
    suite = 1 
    print (suite)
elif len(days)==2 :  
    suite = 2
    print (suite)
else :  
    suite = 3
    print (suite)
    
    
a=input("请输入第一个数a=")
b=input("请输入第二个数b=")
if a > b :
    print("a大于b")
elif a < b :
    print("a小于b")
else : 
    print("a等于b")
# 用while循环的话，必须有一个计数器
count=0 #计数器，控制循环次数
# 循环就是重复执行循环体里面的代码
while count<10:
    print('test'+str(count))
    count=count+1
    #每次循环加1，也可以这样写
    # count+=1
    
for a in range(5):
    print(a) #a是内部定义的一个计数器，会自增,用其他字母都行

count=0
while count<3:
    name=input('请输入你的名字：')
    print('你输入的名字是：',name)
    if name=='quit':
        break #结束循环，在循环里面遇到break，不管还有多少次循环，立即结束整个循环
    count+=1
count =0
while count<5:
    print('hahahaha')
    count+=1
    if count==2:
        continue #结束本次循环，下面的代码不执行了,从第一行又开始执行
    else :
        count+=1
