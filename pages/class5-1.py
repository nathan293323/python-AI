import streamlit as st
import time
import os

# 設計products字典，每個商品有價格(price)、圖片(image)、庫存(stock)、圖片(image)三個屬性
# image可以讀取存放在image資料夾中的圖片
# 讀取圖片清單

image_folder = "image"  # 資料夾名稱
image_files = os.listdir(image_folder)  # 取得資料夾裡面的所有檔案

if "products" not in st.session_state:
    st.session_state.products = {}  # 建立products字典

for image_file in image_files:
    product_name = image_file[:-4]  # 去掉副檔名
    if product_name not in st.session_state.products:  # 如果商品不存在，就新增商品
        st.session_state.products[product_name] = {
            "price": 10,
            "stock": 10,
            "image": f"{image_folder}/{image_file}",
        }
# products 範例
# products = {"香蕉" : {"price": 10, "stock": 10, "image": "image/香蕉.jpg"},
# "橘子" : {"price": 20, "stock": 5, "image": "image/橘子.jpg"},
# "蘋果" : {"price": 15, "stock": 3, "image": "image/蘋果.jpg"}}

# 顯示商品
st.title("購物平台")  # 標題
col_cum = st.number_input("欄數", min_value=1, step=1, value=2)
cols = st.columns(col_cum)
i = 0
for product_name, detail in st.session_state.products.items():
    with cols[i % col_cum]:  # 透過取餘數來決定商品顯示哪一欄
        st.image(detail["image"], use_column_width=True)
        st.markdown(f"### {product_name}")
        st.markdown(f"價格：${detail['price']}")
        st.markdown(f"庫存：{detail['stock']}")

        if st.button(f"購買{product_name}", key=f"{product_name}"):
            if detail["stock"] > 0:
                st.session_state.products[product_name]["stock"] -= 1
                st.success(f"購買{product_name}成功")
                time.sleep(1)
                st.rerun()
            else:
                st.error(f"{product_name}庫存不足!")
    i += 1

# 新增商品庫存數量
st.title("新增商品庫存")
product_names = list(st.session_state.products.keys())
col1, col2 = st.columns(2)
with col1:
    selected_product = st.selectbox("選擇商品", product_names)
with col2:
    new_stock = st.number_input("庫存數量", min_value=1, step=1)

if st.button("新增庫存"):
    st.session_state.products[selected_product]["stock"] += new_stock
    st.success(f"{selected_product}的庫存已新增{new_stock}件")
    time.sleep(1)
    st.rerun()

# 重新顯示商品以反映更新後的庫存
st.markdown("目前商品庫存")
for product_name, details in st.session_state.products.items():
    st.markdown(f"### {product_name}: {details['stock']} 件")
