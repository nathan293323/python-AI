# append方法
l = [1, 2, 3]
l.append(4)
print(l)

# remove方法
l = ["a", "b", "c"]
l.remove("a")
print(l)

# count方法
l = [9, 1, -4, 3, 7, 11, 3]
print(l.count(3))

L = [9, 1, -4, 3, 7, 11, 3]  # 這是一個有10個元素的list
c = L.count(3)  # 計算L中有幾個3
for i in range(c):  # 把L中所有3從L中刪除
    L.remove(3)
print(L)  # 印出L

# pop方法
L.pop(0)  # 把L中的第0個元素刪除
print(L)  # 印出L
# ppop和remove的差別，pop 是用index, remove是用元素來刪除

# sort方法
l = [3, 1, 2, 4, 5]  # 由小到大排序
l.sort()
print(l)

# reverse方法   反轉序列
l = [3, 1, 2, 4, 5]
l.reverse()
print(l)

# index方法 找元素的標籤
l = [3, 1, 2, 4, 5]
print(l.index(3))
