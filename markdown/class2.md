## 比較運算

```python
print(1 == 1)  # 比較是否相等的運算
print(1 != 1)  # 比較是否不相等的運算
print(1 > 1)  # 比較是否大於的運算
print(1 < 1)  # 比較是否小於的運算
print(1 >= 1)  # 比較是否大於或等於的運算
print(1 <= 1)  # 比較是否小於或等於的運算
```

## 邏輯運算

```python
print(not True)  # 邏輯非運算
print(not False)  # 邏輯非運算

print(True and True)  # 邏輯且運算
print(True and False)  # 邏輯且運算
print(False and True)  # 邏輯且運算
print(False and False)  # 邏輯且運算

print(True or True)  # 邏輯或運算
print(True or False)  # 邏輯或運算
print(False or True)  # 邏輯或運算
print(False or False)  # 邏輯或運算
```

## 運算優先順序

1. ()
2. **
3. * / // %
*. + -
5. == != > < >= <=
6. not、and、or

## 條件判斷

```python
pwd = input("請輸入密碼:")
if pwd == "123":
    print("密碼正確")
elif pwd == "456":
    print("密碼正確")
else:
    print("密碼錯誤")

# 判斷一定是 if 開頭, if只能有一個
# 判斷可以有無限多個elif, 也可以沒有
# 判斷可以有一多個else, 也可以沒有
# elif和else都是有選擇性
```

## Streamlit

```python
import streamlit as st

number = st.number_input("輸入一個數字", step=1)
st.markdown(f"你輸入的數字是{number}")

grade = st.number_input("輸入你的分數", step=1, min_value=0, max_value=100)
st.markdown(f"你輸入的分數是{grade}")

if grade >= 90 and grade <= 100:
    st.markdown("你的等級是A")
elif grade >= 80 and grade <= 89:
    st.markdown("你的等級是B")
elif grade >= 70 and grade <= 79:
    st.markdown("你的等級是C")
elif grade >= 60 and grade <= 69:
    st.markdown("你的等級是D")
else:
    st.markdown("你的等級是F")

st.title("按鈕元件練習")
st.button("點我", key="button1")
if st.button("點我", key="button2"):
    st.balloons()
```

## 迴圈

```python
for i in range(10):  # i 是迴圈的變數, range(10) 是從 0 到 9 的數字
    print(i)  # i 每次只從range(10)內取出一個數字, 從0到9

for i in range(2, 100):  # range(2, 100) 是從 2 到 99 的數字
    print(i)  # i 每次只從range(2, 100)內取出一個數字, 從2到99

for i in range(2, 100, 2):  # range(2, 100, 2) 是從 2 到 99 的數字, 每次取出的數字是偶數
    print(i)  # i 每次只從range(2, 100, 2)內取出一個數字, 從2到99的偶數

for i in range(100, 3, -2):  # range(100, 3, -2) 是從 100 到 4的數字, 每次取出的數字是偶數
    print(i)  # i 每次只從range(100, 3, -2)內取出一個數字, 從100 到 4 的偶數
```

## Streamlit 範例

```python
import streamlit as st

st.title("數字金字塔")
number = st.number_input("輸入一個整數1到9", step=1, min_value=1, max_value=9)
st.markdown("數字金字塔:")
for i in range(1, number + 1):
    st.markdown(str(i) * i)

st.title("箭頭金字塔")
number = st.number_input("輸入箭頭大小:", step=1, min_value=1)
arrow = ""
for i in range(1, number * 2, 2):
    arrow += " " * ((number * 2 - i) // 2) + "*" * i + "\n"
for i in range(number):
    arrow += " " * (number - 1) + "*" + "\n"
st.markdown(f"```\n箭頭金字塔:\n{arrow}\n```")
```

## List 操作

```python
print([])  # 空的list
print([1, 2, 3])  # 有三個元素的list
print([1, 2, 3, "a", "b", "c"])  # 有六個元素的list
print([1, 2, 3, ["a", "b", "c"]])  # 有四個元素的list

L = ["a", "b", "c", "d"]
