import streamlit as st
import datetime
import random

# 1. 페이지 설정
st.set_page_config(
    page_title="🍿 무비 데이: 오늘의 추천",
    page_icon="🎬",
    layout="wide"
)

# 2. 커스텀 CSS (세련된 다크 모드 & 카드 스타일)
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    .movie-card {
        background-color: #1E2129;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #3E4451;
        text-align: center;
        transition: transform 0.3s;
        margin-bottom: 20px;
    }
    .movie-card:hover {
        transform: translateY(-10px);
        border-color: #FF4B4B;
    }
    .genre-tag {
        background-color: #FF4B4B;
        color: white;
        padding: 5px 15px;
        border-radius: 50px;
        font-size: 0.8em;
        font-weight: bold;
    }
    h1, h2, h3 {
        color: #FF4B4B !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 영화 데이터베이스 (예시 데이터)
# 실제 서비스 시에는 API를 연결하거나 더 많은 데이터를 넣을 수 있습니다.
movie_db = {
    "로맨스 💖": [
        {"title": "어바웃 타임", "desc": "매일매일을 마지막 날처럼 살기.", "emoji": "⏳"},
        {"title": "라라랜드", "desc": "꿈꾸는 바보들을 위하여.", "emoji": "💃"},
        {"title": "비포 선라이즈", "desc": "우연히 만난 운명 같은 하룻밤.", "emoji": "🌅"}
    ],
    "SF/액션 🚀": [
        {"title": "인터스텔라", "desc": "우리는 답을 찾을 것이다, 늘 그랬듯이.", "emoji": "🪐"},
        {"title": "인셉션", "desc": "생각은 가장 강력한 바이러스다.", "emoji": "🌀"},
        {"title": "매드맥스", "desc": "기억해줘! 최고의 날이었음을.", "emoji": "🔥"}
    ],
    "코미디/힐링 🍀": [
        {"title": "인턴", "desc": "경험은 결코 늙지 않는다.", "emoji": "💼"},
        {"title": "포레스트 검프", "desc": "인생은 초콜릿 상자와 같은 거야.", "emoji": "🍫"},
        {"title": "월터의 상상은 현실이 된다", "desc": "세상을 보고 장애물을 뛰어넘는 것.", "emoji": "📸"}
    ],
    "스릴러/미스터리 🔍": [
        {"title": "기생충", "desc": "가장 한국적인 것이 가장 세계적인 것.", "emoji": "🍑"},
        {"title": "나이브스 아웃", "desc": "누구도 믿을 수 없는 저택 살인사건.", "emoji": "🔪"},
        {"title": "셔터 아일랜드", "desc": "진실은 안개 속에 가려져 있다.", "emoji": "🌫️"}
    ]
}

# 4. 오늘의 날짜를 기준으로 영화 선택 (매일 변경됨)
today_seed = datetime.date.today().strftime("%Y%m%d")
random.seed(today_seed)

# 5. 헤더 섹션
st.title("🎬 𝐎𝐔𝐑 𝐌𝐎𝐕𝐈𝐄 𝐃𝐀𝐘")
st.write(f"### 오늘은 **{datetime.date.today().strftime('%Y년 %m월 %d일')}**")
st.markdown("당신의 오늘 하루를 완벽하게 만들어줄 장르별 추천 영화입니다. ✨")
st.write("")

# 6. 메인 화면 레이아웃 (2개씩 2줄 배치)
cols = st.columns(2)

for i, (genre, movies) in enumerate(movie_db.items()):
    # 날짜 시드에 맞춰 매일 하나의 영화를 무작위로 뽑음
    daily_movie = random.choice(movies)
    
    with cols[i % 2]:
        st.markdown(f"""
            <div class="movie-card">
                <span class="genre-tag">{genre}</span>
                <h1 style='font-size: 50px; margin-top: 10px;'>{daily_movie['emoji']}</h1>
                <h2>{daily_movie['title']}</h2>
                <p style='color: #B0B0B0; font-style: italic;'>"{daily_movie['desc']}"</p>
            </div>
            """, unsafe_allow_html=True)
        
        # 버튼 클릭 시 추가 정보 (Streamlit 기본 위젯 활용)
        with st.expander(f"{daily_movie['title']} 정보 더 보기 ℹ️"):
            st.write(f"이 영화는 **{genre}** 장르의 명작입니다.")
            st.write("관련 플랫폼: 넷플릭스, 디즈니+, 티빙 등")
            if st.button(f"'{daily_movie['title']}' 찜하기 ❤️", key=genre):
                st.toast(f"'{daily_movie['title']}' 영화가 찜 목록에 추가되었습니다! 🍿")

# 7. 하단 푸터
st.markdown("---")
st.caption("📷 영화 데이터는 매일 자정에 자동으로 업데이트됩니다.")
st.snow() # 겨울 느낌 혹은 분위기 효과
