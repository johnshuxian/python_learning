import random

secret = random.randint(1,10)

print('-----猜一猜我想的数字是什么？---------')
temp = input("猜一猜：")
guess = int(temp)

while guess != secret:
    temp = input("猜错了，再试试：")
    guess = int(temp)
    if guess == secret:
        print('恭喜你，猜对了')
    else:
        if guess > secret:
            print('不对哦，大了哦')
        else:
            print('嘿嘿，猜小了哦')
print('游戏结束')