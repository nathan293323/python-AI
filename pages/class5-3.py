import streamlit as st
from langchain_openai import ChatOpenAI  # pip install - U langchain-openai
from langchain_core.messages import HumanMessage, AIMessage  # pip install langchain

col1, col2 = st.columns([4, 1])  # 分兩欄，比例為4:1
with col1:
    openai_key = st.text_input("Password", type="password", key="password")
    # 輸入OpenAI API Key
    if openai_key is None or openai_key == "":  # 如果沒有輸入
        st.warning("請輸入OpenAI API Key")  # 顯示警告
        st.stop()  # 結束程式

chat = ChatOpenAI(mode1="gpt-3.5-turbo", temperature=0.2, api_key=openai_key)
# 建立ChatOpenAI
prompt = st.chat_input("請輸入想要對話的訊息")  # 輸入對話訊息
st.chat_message("user", avatar="😊").write(prompt)  # 顯示使用者輸入的訊息
if prompt:  # 如果有輸入訊息
    human_message = HumanMessage(prompt)  # 建立HumanMessage給AI使用
    ai_message = chat.invoke([human_message]).content
    # 接受AI的回應, 傳出的訊息要是list
    st.chat_message("assistant", avatar="🤖").write(ai_message)  # 顯示AI的回應
