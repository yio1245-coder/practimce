import streamlit as st
import time

# 페이지 설정 (가장 상단에 위치해야 합니다)
st.set_page_config(
    page_title="✨MBTI 미래 설계소✨",
    page_icon="🚀",
    layout="centered"
)

# --- 커스텀 CSS (화려한 스타일링) ---
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border: None;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff7575;
        transform: scale(1.02);
    }
    .result-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-left: 5px solid #FF4B4B;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 타이틀 및 헤더 ---
st.title("🚀 MBTI 맞춤형 진로 탐험대")
st.subheader("나의 성격 유형에 딱 맞는 직업은 무엇일까요? ✨")
st.markdown("---")

# --- 데이터 정의 ---
mbti_jobs = {
    "ISTJ": {"job": "공인회계사, 법률 전문가, 군 장교", "desc": "철저하고 체계적인 당신은 신뢰받는 관리자!", "emoji": "💼"},
    "ISFJ": {"job": "간호사, 초등교사, 사회복지사", "desc": "헌신적이고 따뜻한 당신은 진정한 수호자!", "emoji": "🛡️"},
    "INFJ": {"job": "상담심리사, 작가, 환경 운동가", "desc": "통찰력 있는 당신은 세상을 바꾸는 예언자!", "emoji": "🔮"},
    "INTJ": {"job": "데이터 과학자, 전략 기획가, 건축가", "desc": "분석적이고 독립적인 당신은 냉철한 전략가!", "emoji": "🧠"},
    "ISTP": {"job": "소프트웨어 개발자, 엔지니어, 조종사", "desc": "손재주가 좋고 논리적인 당신은 만능 재주꾼!", "emoji": "🛠️"},
    "ISFP": {"job": "그래픽 디자이너, 사진작가, 작곡가", "desc": "예술적 감각이 뛰어난 당신은 호기심 많은 예술가!", "emoji": "🎨"},
    "INFP": {"job": "소설가, 예술 치료사, 유튜버", "desc": "이상주의적이고 감성이 풍부한 당신은 열정적인 중재자!", "emoji": "🌻"},
    "INTP": {"job": "물리학자, 프로그래머, 철학자", "desc": "논리적이고 호기심 많은 당신은 아이디어뱅크!", "emoji": "🧪"},
    "ESTP": {"job": "기업가, 소방관, 스포츠 매니저", "desc": "활동적이고 적응력이 빠른 당신은 모험을 즐기는 사업가!", "emoji": "⚡"},
    "ESFP": {"job": "연예인, 이벤트 플래너, 홍보 전문가", "desc": "에너지가 넘치는 당신은 자유로운 영혼의 연예인!", "emoji": "🎭"},
    "ENFP": {"job": "광고 카피라이터, 파티 플래너, 기자", "desc": "재기발랄하고 상상력이 풍부한 당신은 활동가!", "emoji": "🌈"},
    "ENTP": {"job": "정치인, 발명가, 마케팅 디렉터", "desc": "변론을 즐기고 창의적인 당신은 뜨거운 설전의 변론가!", "emoji": "💡"},
    "ESTJ": {"job": "경영인, 경찰관, 프로젝트 매니저", "desc": "추진력 있고 엄격한 당신은 유능한 경영자!", "emoji": "📊"},
    "ESFJ": {"job": "호텔리어, 승무원, 홍보 담당자", "desc": "친절하고 사교적인 당신은 조화로운 외교관!", "emoji": "🤝"},
    "ENFJ": {"job": "인사관리자, 시민단체 활동가, 교사", "desc": "카리스마 넘치고 영향력 있는 당신은 정의로운 선도자!", "emoji": "📢"},
    "ENTJ": {"job": "CEO, 경영 컨설턴트, 변호사", "desc": "결단력 있고 통솔력이 강한 당신은 대담한 통치자!", "emoji": "👑"},
}

# --- 사용자 입력 ---
col1, col2 = st.columns([1, 1])

with col1:
    st.write("### 🔍 나의 MBTI 선택")
    selected_mbti = st.selectbox(
        "리스트에서 선택해주세요 👇",
        options=list(mbti_jobs.keys())
    )

with col2:
    st.write("### 🎁 행운의 이모지")
    if selected_mbti:
        st.header(mbti_jobs[selected_mbti]["emoji"])

# --- 결과 출력 ---
if st.button("내 미래 직업 확인하기! ✨"):
    with st.spinner('당신의 미래를 분석 중입니다... ⏳'):
        time.sleep(1.5)  # 화려한 효과를 위한 로딩 시간
    
    st.balloons()  # 축하 효과!
    
    data = mbti_jobs[selected_mbti]
    
    st.markdown(f"""
    <div class="result-card">
        <h2>{selected_mbti} 유형을 위한 추천 🌈</h2>
        <p style='font-size: 1.2em;'><b>" {data['desc']} "</b></p>
        <hr>
        <h4>📍 추천 직업군</h4>
        <p style='font-size: 1.3em; color: #FF4B4B;'><b>{data['job']}</b></p>
    </div>
    """, unsafe_allow_html=True)

# --- 하단 안내 ---
st.markdown("---")
st.info("💡 이 결과는 성격 유형에 따른 일반적인 추천이며, 여러분의 가능성은 무한합니다! 💪")
