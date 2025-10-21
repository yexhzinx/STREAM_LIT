import streamlit as st
from datetime import datetime, date
import pandas as pd
import numpy as np

# --------------------------
# 페이지 설정
# --------------------------

st.set_page_config(
    page_title="스트림릿 UI 가이드",            # 브라우저 탭 제목
    page_icon="🎉",                          # 브라우저 탭 아이콘 (이모지 또는 이미지 경로)
    layout="wide",                            # 페이지 레이아웃 ('centered' | 'wide')
    initial_sidebar_state="collapsed",        # 사이드바 초기 상태 ('auto' | 'expanded' | 'collapsed')  
        menu_items={                                # 우측 상단 메뉴 커스터마이징
        'Get Help': 'https://docs.streamlit.io/',         # "Get help" 메뉴 링크
        'Report a bug': 'https://github.com/streamlit',   # "Report a bug" 메뉴 링크
        'About': '이 앱은 Streamlit 가이드용 예시입니다.'    # "About" 메뉴 내용
    }
)

# --------------------------
# 제목 / 텍스트
# --------------------------

st.title("스트림릿 UI 단계별 가이드")
st.header("1단계 : 텍스트 표시")
st.subheader("다양한 텍스트 스타일")

st.write("일반 텍스트를 표시합니다.")
st.markdown("**굵은 글씨**와 *기울임* 그리고 `코드` 형식도 가능합니다.")
st.caption("작은 캠션 텍스트입니다.")
st.code("print('코드 블록 예제')", language="python")

st.divider()

# --------------------------
# 입력 위젯 - 1
# --------------------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("텍스트 입력")
    text_input = st.text_input("이름을 입력하세요", placeholder="홍길동")
    text_area = st.text_area("메시지를 입력하세요", placeholder="여기에 입력...")
    number_input = st.number_input("숫자를 입력하세요", min_value=0, max_value=100, value=50)
    # 이벤트 처리
    st.write('text_input', text_input)
    if text_input:
        st.success(f"이름 : (text_input)")
    if text_area:
        st.success(f"메세지 : (text_area)")
    if number_input:
        st.success(f"숫자 : (number_input)")

with col2:
    st.subheader("두번째 컬럼")
    selectbox = st.selectbox("옵션을 선택하세요", ["옵션1", "옵션2", "옵션3"])
    multiselect = st.multiselect("여러 개 선택 가능", ["A", "B", "C", "D"])
    radio = st.radio("하나만 선택", ["예", "아니오", "모름"])

    st.write('selectbox', selectbox)
    st.write('multiselect', multiselect)
    st.write('radio', radio)

st.divider()

# --------------------------
# 입력 위젯 - 2
# --------------------------

st.header("3단계: 날짜 및 시간 입력")

col1, col2, col3 = st.columns(3)

with col1:
    date_input = st.date_input("날짜 선택", value=date.today())
    st.write(f"date_input : {date_input}")

with col2:
    time_input = st.time_input("시간 선택")
    st.write(f"time_input : {time_input}")

with col3:
    slider = st.slider("슬라이더", 0, 100, 50)
    st.write(f"slider : {slider}")

st.divider()

# --------------------------
# 입력 위젯 - 3
# --------------------------

col1, col2 = st.columns(2)

with col1:
    checkbox1 = st.checkbox("동의합니다", value=True)
    checkbox2 = st.checkbox("뉴스레터 구독")
    checkbox3 = st.checkbox("마케팅 수신 동의")

    st.write(f"checkbox1 : {checkbox1}")
    st.write(f"checkbox2 : {checkbox2}")
    st.write(f"checkbox3 : {checkbox3}")


with col2:
    toggle1 = st.toggle("알림 활성화", value=True)
    toggle2 = st.toggle("다크모드")
    toggle3 = st.toggle("자동 저장")
    
    st.write(f"toggle1 : {toggle1}")
    st.write(f"toggle2 : {toggle2}")
    st.write(f"toggle3 : {toggle3}")

st.divider()

# --------------------------
# 버튼
# --------------------------

st.header("3단계 : 버튼")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("일반 버튼", type="primary"):
        st.success("버튼이 클릭되었습니다!")

with col2:
    if st.button("보조 버튼", type="secondary"):
        st.info("보조 버튼 클릭!")

with col3:
    if st.download_button("다운로드", data="샘플 데이터", file_name="sample.txt"):
        st,success("다운로드 시작!")

with col4:
    # 임시 데이터 프레임 생성
    df_tmp = pd.DataFrame({
        '이름' : ["김범수", "박효신", "박정현"],
        '나이' : [40,45,42],
        '주소' : ['서울', '부산', '대구']
    })  
    df_tmp.to_csv('/app/dataSet/학생점수.csv', index=False, encoding="utf-8-sig")

    with open('/app/dataSet/학생점수.csv', 'rb') as f:
        st.download_button(
            label="학생점수파일 다운로드",
            data=f,
            file_name="학생점수.csv",
            mime="text/csv"
        )

st.divider()

# --------------------------
# 테이블
# --------------------------

st.header("4단계 : 테이블 생성")

col1, col2 = st.columns(2)
# 샘플 데이터 생성
df_tbl = pd.DataFrame({
    '이름': ['김철수', '이영희', '박민수', '최지연'],
    '나이': [25, 30, 35, 28],
    '점수': [85, 92, 78, 95],
    '등급': ['B', 'A', 'C', 'A']
})

with col1:
    st.subheader("일반 테이블")
    st.write(df_tbl)

with col2:
    st.subheader("데이터 프레임")
    st.dataframe(
        df_tbl,
        use_container_width=True,
        hide_index=True,
        column_config={
        # '나이' 열에 바 차트 적용(최대값 40 가정)
        "나이": st.column_config.ProgressColumn(
            "나이 게이지",
            help="나이를 최대 50세 기준으로 표시합니다.",
            format="%d세",      # 숫자 뒤에 '세'를 붙여 표시
            min_value=0,
            max_value=100,      # 게이지의 최대값 설정
            ),
        }   

    )

st.subheader("편집 가능 테이블")
st.data_editor(df_tbl, num_rows="dynamic")

st.divider()

# --------------------------
# 차트 만들기
# --------------------------

st.header("5단계 : 차트만들기")

df_chart = pd.DataFrame(np.random.randn(20,3), columns=['A', 'B', 'C'])
# st.write(df_chart)

col1, col2 = st.columns(2)

with col1:
    st.subheader("라인 차트")
    st.line_chart(df_chart)

with col2:
    st.subheader("영역 차트")
    st.area_chart(df_chart)

col1, col2 = st.columns(2)

with col1:
    st.subheader("막대 차트")
    st.bar_chart(df_chart)

with col2:
    st.subheader("산점도 차트")
    st.scatter_chart(
        df_chart,
        x='A',  # x축 컬럼 지정
        y='B',  # y축 컬럼 지정
        size='C',   # 점의 크기를 'C' 컬럼 값에 따라 다르게 지정(선택적)
        color='C',  # 점의 색상을 'C' 컬럼 값에 따라 다르게 지정(선택적)
    )

st.divider()

# --------------------------
# 알림 메시지
# --------------------------

st.header("6단계 : 알림메시지")

col1, col2 = st.columns(2)

with col1:
    st.success("성공 메시지입니다!")
    st.info("정보  메시지입니다!")

with col2:
    st.warning("경고 메시지입니다!")
    st.error("오류 메시지입니다!")

st.divider()

# --------------------------
# 프로그래스바
# --------------------------

st.header("7단계 : 프로그레스 바와 스피너")

value = st.number_input("진행률(%) 입력 : ", min_value=0, max_value=100, step=1)

import time
progress_bar = st.progress(0)
spinner = st.spinner("진행중 :")
if value>0 : 
    with spinner:
        for i in range(int(value)) :
            progress_bar = st.progress(i+1)
            time.sleep(0.05)
    st.success("처리 완료")

st.divider()

# --------------------------
# 업로드
# --------------------------
import os

st.header("8단계 : 파일 업로드")  

col1, col2 = st.columns(2)

with col1:
    #IN MEMORY 방식으로 파일 업로드(주기억장치 임시저장)
    st.subheader("IN MEMORY 방식")
    uploaded_file_1 = st.file_uploader("파일을 선택하세요", type=['csv', 'txt', 'xlsx'], key="uploader_1")
    if uploaded_file_1:
        st.success(f"파일 업로드 성공 : {uploaded_file_1.name}")
        st.success(f"파일 크기 : {uploaded_file_1.size} byte")

with col2:
    #FILE SYSTEM 방식으로 파일 업로드(보조기억장치 영구저장)
    st.subheader("FILE SYSTEM 방식")
    SAVE_DIR_PATH = "/app/dataSet"
    os.makedirs(SAVE_DIR_PATH, exist_ok=True) # 폴더 없으면 자동 생성
    uploaded_file_2 = st.file_uploader("파일을 선택하세요", type=['csv', 'txt', 'xlsx'], key="uploader_2")

    if uploaded_file_2 is not None:
        # 파일경로설정
        save_path = os.path.join(SAVE_DIR_PATH, uploaded_file_2.name) # /app/dataSet/filename
        # 파일저장
        with open(save_path, "wb") as f:
            f.write(uploaded_file_2.getbuffer())
        
        st.success(f"파일 업로드 성공 : {uploaded_file_2.name}")
        st.success(f"파일 업로드 크기 : {uploaded_file_2.size} byte")
        st.success(f"파일 저장 경로 : {save_path}")



