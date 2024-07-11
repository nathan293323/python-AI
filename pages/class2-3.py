# 迴圈筆記
for i in range(10):  # i 是迴圈的變數, rande(10) 是從 0 到 9 的數字
    print(i)  # i 每次只從range(10)內取出一個數字, 從0到9

for i in range(2, 100):  # range(2, 100) 是從 2 到 99 的數字
    print(i)  # i 每次只從range(2, 100)內取出一個數字, 從2到99

for i in range(2, 100, 2):  # range(2, 100, 2) 是從 2 到 99 的數字, 每次取出的數字是偶數
    print(i)  # j 每次只從range(2, 100, 2)內取出一個數字, 從2到99的偶數

for i in range(100, 3, -2):
    # range(100, 3, -2) 是從 100 到 4的數字, 每次取出的數字是偶數
    print(i)  # j 每次只從range(100, 3, -2)內取出一個數字, 從100 到 4 的偶數
