import streamlit as st
import os

folderpath = "markdown"  # 這是相對路徑, C:\Users\USER\Desktop\python-AI\markdown
files = os.listdir(folderpath)  # 列出資料夾中所有文件
files_name = []  # 建立一個空的list準備存需要的檔案
for f in files:
    if f.endswith(".md"):  # 印出所有markdown文件
        files_name.append(f)  # 把檔案加到files_name中

for f in files_name:  # 逐一讀取files_name中的檔案
    with open(f"{folderpath}/{f}", "r", encoding="utf-8") as file:  # 開啟檔案
        content = file.read()  # 讀取檔案內容
    with st.expander(f[:-3]):  # 建立一個擴展元件,標題是檔案名稱
        st.markdown(content)  # 把檔案內容顯示在擴展元件中
