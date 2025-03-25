import streamlit as st

st.set_page_config("Chat_with_blog_and_website")

st.markdown("<h2 style='text-align:center;'> Chat with Blog and Website</h2>", unsafe_allow_html=True)

col1,col2 = st.columns(2)

with col1:
    first = st.button("Chat with Blog/ Website")

with col2:
    second = st.button("Summarize Blog/ Website")

if first:
    st.success("first")

elif second:
    st.info("secodn")