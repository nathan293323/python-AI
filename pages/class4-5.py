import streamlit as st
import os

st.title("購物平台")
image_folder = "image"  # 資料夾名稱
image_files = os.listdir(image_folder)  # 取得資料夾裡面的所有檔案
st.write(image_files)  # 顯示所有檔案

image_size = st.number_input("圖片大小", min_value=1, step=1, value=1)
for image_file in image_files:  # 顯示所有圖片
    st.image(
        f"{image_folder}/{image_file}",
        width=image_size,
    )
    # 顯示圖片, 根據使用者輸入的大小調整寬度

for image_file in image_files:  #  顯示所有圖片
    st.image(f"{image_folder}/{image_file}", use_column_width=True)
    # 顯示圖片, 使用欄寬度
