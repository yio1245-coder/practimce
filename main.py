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
        {"title": "매드
