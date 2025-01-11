import streamlit as st

from utils import generate_xiaohongshu

openai_api_key = "sk-a8acecc0a0aa4bc5a0ff27c8fe8f42c8"


st.header("爆款小红书AI写作助手 ✏️")

theme = st.text_input("主题")
submit = st.button("开始写作")

if submit and not theme:
    st.info("请输入生成内容的主题")
    st.stop()
    
if submit:
    with st.spinner("AI正在努力创作中，请稍等..."):
        result = generate_xiaohongshu(theme, openai_api_key)
    st.divider()
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("##### 小红书标题1")
        st.write(result.titles[0])
        st.markdown("##### 小红书标题2")
        st.write(result.titles[1])
        st.markdown("##### 小红书标题3")
        st.write(result.titles[2])
        st.markdown("##### 小红书标题4")
        st.write(result.titles[3])
        st.markdown("##### 小红书标题5")
        st.write(result.titles[4])
    with right_column:
        st.markdown("##### 小红书正文")
        st.write(result.content)
