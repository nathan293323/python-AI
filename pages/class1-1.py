# 註解筆記
# 有註解的行
"""
使用多行註解
"""
# print("Hello World!") # ctrL+? 可以單行註解
print("123")  # 可以在code後面加上'#'來當作註解

# ctrl+s代表存檔
# ctrl+右或左可以部份註解
print(123)  # 整數
print(123.456)  # 浮點數
print("hello")  # 字串
print(True)  # 布林值
print("false")  # 布林值
print('"')  # 印出雙引號
print("'")  # 印出單引號

a = 10  # 把10存到變數a的空間, =就是將右邊的值存到左邊的變數空間
print(a)

b = "hello"  # 把hello存到變數b的空間, =就是將右邊的值存到左邊的變數空間
print(b)

print(1 + 1)  # 加法計算
print(1 - 1)  # 減法計算
print(1 * 1)  # 乘法計算
print(1 / 1)  # 除法計算
print(10 // 3)  # 整數除法計算
print(10 % 3)  # 取餘數
print(2**3)  # 次方 2**3 = 2*2*2 = 8

# 符號的優先順序
# 1.()
# 2.**
# 3.* / // %
# 4.+ -

# 字串運算
a = "hello"
b = "world"
print(a + b)  # 字串加法
print(a + " " + b)  # 字串相加
print(a * 3)  # 字串乘法
# 加法乘法混合
print(a + " " + b * 3)  # 字串相加

print(f"hello{10}{True}")
# 字串前加f, 可以在字串中加上其他變數， 用{}包住變數

print(len("hello"))  # 字串長度
print(int("123"))  # 字串轉整數
print(float("123.456"))  # 字串轉浮點數
print(bool("true"))  # 字串轉布林值
print(str(123))  # 整數轉字串


print("input()可以在終端機輸入文字")
a = input("在這邊可以輸入文字")  # input()可以在終端機輸入文字
print(f"你輸入的內容是:{a}")  # 印出輸入的文字
print(f"input()輸入的內容型態是:{type(a)}")  # 輸入的內容型態是字串

# 計算正方形面積
a = input("輸入正方形的邊長:")
area = int(a) * int(a)
print(f"正方形的面積是:{area}")
