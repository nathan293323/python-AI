# 程式技巧筆記

## 註解

### 單行註解

- 使用 `#` 來進行單行註解。

```python
# 這是一個單行註解
print("Hello World!")  # 這也是單行註解
```

### 多行註解

-單引號 `'''` 來進行多行註解。

```python
'''
這是一個多行註解
'''
```

## 印出不同類型的數值和字串

- 使用 `print()` 函數來印出不同類型的數值和字串。

```python
print(123)  # 整數
print(123.456)  # 浮點數
print("hello")  # 字串
print(True)  # 布林值
print("false")  # 字串
print('"')  # 印出雙引號
print("'")  # 印出單引號
```

## 變數賦值

- 使用 `=` 來將值賦給變數。

```python
a = 10  # 將10賦值給變數a
b = "hello"  # 將字串hello賦值給變數b
print(a)
print(b)
```

## 基本算術運算

- 加法: `+`
- 減法: `-`
- 乘法: `*`
- 除法: `/`
- 整數除法: `//`
- 取餘數: `%`
- 次方: `**`

```python
print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法
print(10 // 3)  # 整數除法
print(10 % 3)  # 取餘數
print(2**3)  # 次方
```

## 運算符的優先順序

1. `()`
2. `**`
3. `* / // %`
4. `+ -`

## 字串運算

- 字串相加: `+`
- 字串相乘: `*`

```python
a = "hello"
b = "world"
print(a + b)  # 字串相加
print(a + " " + b)  # 字串相加
print(a * 3)  # 字串相乘
print(a + " " + b * 3)  # 混合使用字串相加和相乘
```

## f-string

- 在字串前加上 `f`，可以在字串中嵌入變數，使用 `{}` 包住變數。

```python
print(f"hello{10}{True}")
```

## 內建函數

- `len()`：獲取字串長度
- `int()`：將字串轉換為整數
- `float()`：將字串轉換為浮點數
- `bool()`：將字串轉換為布林值
- `str()`：將數值轉換為字串

```python
print(len("hello"))  # 字串長度
print(int("123"))  # 字串轉整數
print(float("123.456"))  # 字串轉浮點數
print(bool("true"))  # 字串轉布林值
print(str(123))  # 數值轉字串
```

## 使用 `input()` 函數

- `input()` 函數用來從終端機輸入文字，輸入的內容型態是字串。

```python
a = input("在這邊可以輸入文字")
print(f"你輸入的內容是:{a}")
print(f"input()輸入的內容型態是:{type(a)}")
```

## 計算正方形面積的例子

- 使用 `input()` 函數來輸入邊長，並計算正方形的面積。

```python
a = input("輸入正方形的邊長:")
area = int(a) * int(a)
print(f"正方形的面積是:{area}")
```
