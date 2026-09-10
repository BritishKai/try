import streamlit as st

if "step" not in st.session_state:
    st.session_state.step = 0

st.set_page_config(
    page_title="Quiz Time!",
    layout="centered"
)

st.markdown(
    """
    <style>
    .block-container {padding-top: 2rem; padding-bottom: 3rem; max-width: 640px;}
    .stButton>button {
        width: 100%; padding: 0.8em; font-size: 1rem;
        border-radius: 14px; background-color: #ff6b81; color: white; border: none;
    }
    .stButton>button:hover {background-color: #ff4d6d; color: white;}
    </style>
    """,
    unsafe_allow_html=True,
)

total_step = 13

def questions(this_step, key, question, options, answer):
    st.subheader("Pertanyaan")
    jeongdab = st.radio(question, options, index=None, key=key)
    if jeongdab is not None:
        if jeongdab == answer:
            st.success("Benar ༘⋆ヽ( ^ᴗ^)ノ⋆ˎˊ˗")
        else:
            st.error(f"˙◠˙ harusnya {answer} ga sih")
        if st.button("Next", key=f"next_{key}"):
            st.session_state.step += 1
            st.rerun()

def challenge(this_step, key, mission):
    st.subheader("Challenge")
    st.write(mission)
    if st.button("Done, lanjut", key=f"next_{key}"):
        st.session_state.step += 1
        st.rerun()

step = st.session_state.step
st.progress((step + 1) / total_step)

if step == 0:
    questions(0, "q1", "Pertanyaan 1", ["A", "B", "C", "D"], "A")
elif step == 1:
    challenge(1, "c1", "Challenge")
elif step == 2:
    st.balloons()
    st.markdown(
        "<h3 style='text-align:center;'>Happy Anniversary, Bapak & Ibu! 💞</h3>",
        unsafe_allow_html=True,
    )