import streamlit as st
from PIL import Image

# 1. 웹 페이지 설정
st.set_page_config(
    page_title="나의 자기소개 페이지",
    page_icon="👋",
    layout="centered"
)

# 2. 사이드바 구성 (연락처 등 추가 정보)
st.sidebar.header("Contact Info")
st.sidebar.text("📧 email@example.com")
st.sidebar.text("🔗 [GitHub](https://github.com)")

# 3. 메인 화면 구성
st.title("안녕하세요! 저는 [이름]입니다 👋")

# 컬럼을 나누어 사진과 인사말 배치
col1, col2 = st.columns([1, 2])

with col1:
    # 'profile.jpg'라는 이름의 이미지 파일이 필요합니다. 
    # 없다면 샘플 이미지를 불러옵니다.
    try:
        image = Image.open('profile.jpg')
        st.image(image, use_container_width=True)
    except:
        st.image("https://via.placeholder.com/300", caption="프로필 사진을 넣어주세요")

with col2:
    st.subheader("소개")
    st.write("""
    여기에 본인에 대한 설명을 자유롭게 작성하세요.  
    저는 데이터 분석과 웹 개발에 관심이 많은 개발자입니다.  
    Streamlit을 활용해 아이디어를 빠르게 구현하는 것을 좋아합니다!
    """)
    
    # 버튼 클릭 시 축하 메시지 출력
    if st.button("저에게 인사하기"):
        st.balloons()
        st.success("반갑습니다! 방문해주셔서 감사합니다.")

# 4. 기술 스택 섹션
st.divider()
st.subheader("My Skills 🛠️")
skills = ["Python", "Streamlit", "SQL", "Machine Learning"]
st.write(", ".join([f"**{s}**" for s in skills]))

# 5. 간단한 방명록 기능 (상태 저장 X, UI만 구현)
st.divider()
st.subheader("방명록 ✍️")
user_input = st.text_input("남기고 싶은 메시지를 입력하세요:")
if user_input:
    st.write(f"방금 남겨주신 메시지: {user_input}")
