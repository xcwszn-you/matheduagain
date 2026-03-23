import streamlit as st

st.title("🍽️ 점심 메뉴 추천 (가지치기 방식)")
st.write("질문에 답하면서 메뉴를 좁혀가세요. 마지막에 추천 메뉴가 나옵니다!")

# 메뉴 데이터 (가지치기 트리)
menu_tree = {
    "start": {
        "question": "어떤 스타일의 음식을 원하시나요?",
        "options": ["한식", "양식"],
        "next": {"한식": "korean", "양식": "western"}
    },
    "korean": {
        "question": "뜨거운 국물 요리 vs 볶음 요리 중 어떤 걸 선호하시나요?",
        "options": ["국물 요리", "볶음 요리"],
        "next": {"국물 요리": "soup", "볶음 요리": "stir_fry"}
    },
    "western": {
        "question": "파스타 vs 샌드위치 중 어떤 걸 선호하시나요?",
        "options": ["파스타", "샌드위치"],
        "next": {"파스타": "pasta", "샌드위치": "sandwich"}
    },
    "soup": {
        "question": "된장찌개 vs 김치찌개 중 어떤 걸 선택하시겠어요?",
        "options": ["된장찌개", "김치찌개"],
        "next": {"된장찌개": "final_doenjang", "김치찌개": "final_kimchi"}
    },
    "stir_fry": {
        "question": "제육볶음 vs 불고기 중 어떤 걸 선택하시겠어요?",
        "options": ["제육볶음", "불고기"],
        "next": {"제육볶음": "final_jeyuk", "불고기": "final_bulgogi"}
    },
    "pasta": {
        "question": "토마토 파스타 vs 크림 파스타 중 어떤 걸 선택하시겠어요?",
        "options": ["토마토 파스타", "크림 파스타"],
        "next": {"토마토 파스타": "final_tomato", "크림 파스타": "final_cream"}
    },
    "sandwich": {
        "question": "햄 샌드위치 vs 터키 샌드위치 중 어떤 걸 선택하시겠어요?",
        "options": ["햄 샌드위치", "터키 샌드위치"],
        "next": {"햄 샌드위치": "final_ham", "터키 샌드위치": "final_turkey"}
    }
}

# 최종 메뉴
final_menus = {
    "final_doenjang": {"name": "된장찌개 + 밥", "desc": "한국 전통 국물 요리, 따뜻하고 건강한 점심"},
    "final_kimchi": {"name": "김치찌개 + 두부", "desc": "매콤한 국물로 입맛 돋우는 메뉴"},
    "final_jeyuk": {"name": "제육볶음 + 상추", "desc": "달콤 매콤한 고기 요리, 밥과 함께"},
    "final_bulgogi": {"name": "불고기 + 쌈", "desc": "달달한 간장 맛의 전통 고기 요리"},
    "final_tomato": {"name": "토마토 파스타", "desc": "상큼한 토마토 소스로 가벼운 점심"},
    "final_cream": {"name": "크림 파스타", "desc": "부드러운 크림 소스로 풍미 있는 요리"},
    "final_ham": {"name": "햄 샌드위치", "desc": "간단하고 든든한 샌드위치"},
    "final_turkey": {"name": "터키 샌드위치", "desc": "담백한 터키 고기로 건강한 선택"}
}

# 세션 상태 초기화
if "current_step" not in st.session_state:
    st.session_state.current_step = "start"
if "selections" not in st.session_state:
    st.session_state.selections = []

current = st.session_state.current_step

if current.startswith("final_"):
    # 최종 추천
    menu = final_menus[current]
    st.subheader(f"추천 메뉴: {menu['name']}")
    st.write(menu["desc"])
    st.balloons()
    if st.button("다시 시작"):
        st.session_state.current_step = "start"
        st.session_state.selections = []
        st.rerun()
else:
    # 질문 단계
    step_data = menu_tree[current]
    st.subheader(step_data["question"])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button(step_data["options"][0]):
            st.session_state.selections.append(step_data["options"][0])
            st.session_state.current_step = step_data["next"][step_data["options"][0]]
            st.rerun()
    with col2:
        if st.button(step_data["options"][1]):
            st.session_state.selections.append(step_data["options"][1])
            st.session_state.current_step = step_data["next"][step_data["options"][1]]
            st.rerun()

st.markdown("---")
st.write("선택 과정:", " → ".join(st.session_state.selections))
