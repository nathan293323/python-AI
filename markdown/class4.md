# Python 程式筆記

## 條件式迴圈 (`while` 迴圈)

```python
i = 0
while i < 5:  # 當 i < 5 時執行迴圈
    print(i)
    i += 1  # i = i + 1
```

## 算術指定運算子

```python
a = 10
a += 1  # 等同於 a = a + 1
print(a)
a -= 1  # 等同於 a = a - 1
print(a)
a *= 2  # 等同於 a = a * 2
print(a)
a /= 2  # 等同於 a = a / 2
print(a)
a //= 2  # 等同於 a = a // 2
print(a)
a %= 3  # 等同於 a = a % 3
print(a)
a **= 2  # 等同於 a = a ** 2
print(a)
```

## 運算子優先順序

1. `()`
2. `**`
3. `* / // %`
4. `+ -`
5. `== != > < >= <=`
6. `not`, `and`, `or`
7. `= += -= *= /= //= %= **=`

## `break` 跳出迴圈

### `while` 迴圈中使用 `break`

```python
i = 1
while i < 6:  # 當 i < 6 時執行迴圈
    print(i)
    if i == 3:
        break  # 當 i 等於 3 時跳出迴圈
    i += 1
```

### `for` 迴圈中使用 `break`

```python
for i in range(1, 6):  # i 從 1 到 5
    print(i)
    if i == 3:
        break  # 當 i 等於 3 時跳出迴圈
```

## `random` 模組

```python
import random  # 匯入 random 模組

print(random.randrange(10))  # 隨機產生 0 到 9 的整數
print(random.randrange(1, 10))  # 隨機產生 1 到 9 的整數
print(random.randrange(1, 10, 2))  # 隨機產生 1 到 9 的奇數
print(random.randint(1, 10))  # 隨機產生 1 到 10 的整數
```

## 猜數字遊戲

```python
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
```

## 字典操作

### 讀取字典

```python
d = {"星期一": "蘋果", "星期二": "香蕉"}
print(d["星期一"])  # 蘋果
```

### 字典走訪

```python
d = {"星期一": "蘋果", "星期二": "香蕉"}
for key in d:  # 獲得所有的 key
    print(key, d[key])

for key in d.keys():  # 使用 keys() 取得所有的 key
    print(key)

for value in d.values():  # 取得所有的 value
    print(value)  # 蘋果,香蕉

for key, value in d.items():  # 取得所有的 key, value
    print(f"key={key}, value={value}")

for item in d.items():  # 取得所有的 key, value, 存到一個變數裡面
    print(f"key={item[0]}, value={item[1]}")
```

### 元素新增/修改

```python
d = {"星期一": "蘋果", "星期二": "香蕉"}
d["星期一"] = "橘子"  # 修改元素
d["星期三"] = "蘋果"  # 新增元素
print(d)
```

### 檢查 key 是否存在

```python
d = {"星期一": "蘋果", "星期二": "香蕉"}

# key 是否存在於字典中
print("星期一" in d)  # True
print("星期三" in d)  # False

# value 是否存在於字典中
print("蘋果" in d.values())  # True
print("香蕉" in d.values())  # True

L = ["星期一", "星期二"]
print("星期一" in L)  # True
print("星期三" in L)  # False
```

### 刪除元素

```python
d = {"星期一": "蘋果", "星期二": "香蕉"}
d.pop("星期一")  # 刪除 key = "星期一" 的元素
print(d)
d.pop("星期三", "找不到")  # 如果刪除的元素不存在，返回 "找不到"
print(d)
```

## 使用 Streamlit 顯示圖片

```python
import streamlit as st
import os

st.title("圖片文件")
image_folder = "image"  # 資料夾名稱
image_files = os.listdir(image_folder)  # 取得資料夾裡面的所有檔案
st.write(image_files)  # 顯示所有檔案

image_size = st.number_input(
    "圖片大小", min_value=50, max_value=500, step=50, value=100
)  # 使用者輸入圖片大小, 最小50 , 最大500, 預設100, 每次增加50

for image_file in image_files:  # 顯示所有圖片
    st.image(f"{image_folder}/{image_file}", width=image_size)  # 根據使用者輸入的大小調整寬度

for image_file in image_files:  # 顯示所有圖片
    st.image(f"{image_folder}/{image_file}", use_column_width=True)  # 使用欄寬度顯示圖片
```
