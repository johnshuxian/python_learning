score = input("请输入一个分数：")

score = int(score)

if 100>=score>=90:
    print("A")
elif 80<=score<90:
    print("B")
elif 60<=score<80:
    print("C")
elif 0<=score<60:
    print('D')
else:
    print("你输入的是什么鬼东西")