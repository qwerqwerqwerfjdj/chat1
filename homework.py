import streamlit as st

st.title("😀나는 김동하")

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다.
tab1, tab2, tab3 = st.tabs(['나이','이름', '연역'])

with tab1:
    # tab A 를 누르면 표시될 내용
    st.write("")
    st.subheader('내 나이?')
    st.markdown("내 나이는 **19**살")
    st.image("https://m.lovelyco.kr/file_data/lovelyco1004/2021/05/01/03d3a54f037ee78fac3fc2da89c2fc28.jpeg" ,width = 200)

   

with tab2:
    # tab B를 누르면 표시될 내용
    st.write("")
    st.subheader('**김****동****하**')  
    st.caption("▲할아버지가 지어주심^^")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgqnnGWri2XJSqXOxIted9JF2MeUn89g19vL4k2xOHYw&s" ,width = 200)
    st.write("")
    st.write("")

    st.subheader("한자")
    st.markdown('김金  kim  ')
    st.markdown("동桐  dong  ")
    st.markdown("하夏  ha  ")

    




