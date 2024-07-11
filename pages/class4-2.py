import random

ans = random.randrange(1, 101)  # 產生一個 1 到 100 的隨機整數
while True:  # 無窮迴圈
    guess = int(input("請輸入你的猜數(1~100): "))  # 輸入猜數
    if guess < 1 or guess > 100:  # 判斷猜數是否超出範圍
        print("請輸入正確的數字")
    elif guess == ans:  # 判斷猜數是否等於答案
        print("恭喜你,猜對了")
        break  # 當猜數等於答案時跳出迴圈
    elif guess < ans:  # 判斷猜數是否小於答案
        print("再大一點,再猜一次")
    elif guess > ans:  # 判斷猜數是否大於答案
        print("再小一點,再猜一次")
