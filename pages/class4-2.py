import random

ans = random.randrange(1, 101)
guess = input("輸入你的猜數random.randrange(1, 101)")
for guess in range(10):
    if guess == ans:
        print("恭喜你,猜對了")
        break
    elif guess < ans:
        print("再大一點,再猜一次")
    elif guess > ans:
        print("再小一點,再猜一次")
        break
else:
    print("太大了,你猜錯了")
