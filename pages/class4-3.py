print({})  # 空的字典
print({"星期一": "蘋果"})  # 一個 key= 星期一 ,value= 蘋果的字典
print({1: "蘋果", 2: "香蕉"})  # 一個 key= 1 ,value= 蘋果的字典

# 讀取字典
d = {"星期一": "蘋果", "星期二": "香蕉"}
# key 不可以重複,value 可以重複
print(d["星期一"])  # 蘋果


# 字典走訪
d = {"星期一": "蘋果", "星期二": "香蕉"}
for key in d:  # 如果直接將字典當作迴圈範圍, 預設只會獲得 key
    print(key, d[key])

for key in d.keys():  # 可以使用 keys() 取得 所有的key
    print(key)
# 以上兩種方式都是取得 key,結果相同
for value in d.values():  # 取得 所有的value
    print(value)  # 蘋果,香蕉

for key, value in d.items():  # 取得 所有的 key,value分別存到兩個變數裡面
    print(f"key={key},value={value}")
for item in d.items():  # 取得 所有的 key,value,但一起存到一個變數裡面
    print(f"key={item[0]},value={item[1]}")

# 元素新增/修改

d = {"星期一": "蘋果", "星期二": "香蕉"}
d["星期一"] = "橘子"
d["星期三"] = "蘋果"  # 新增元素, 當key不在時會新增元素
print(d)

# 檢查key是否存在
d = {"星期一": "蘋果", "星期二": "香蕉"}
# key 有沒有在字典裡面
print("星期一" in d)  # True
print("星期三" in d)  # False
# value 有沒有在字典裡面
print("蘋果" in d.values())  # True
print("香蕉" in d.values())  # True
L = ["星期一", "星期二"]
print("星期一" in L)  # True
print("星期三" in L)  # False

# 刪除元素
d = {"星期一": "蘋果", "星期二": "香蕉"}
d.pop("星期一")  # 刪除 key = "星期一" 的元素
print(d)
d.pop("星期三", "找不到")  # 如果刪除的元素可能不存在
print(d)
