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
