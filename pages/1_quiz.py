import streamlit as st
from datetime import date, datetime

quiz_open = datetime(2026, 9, 10, 11, 48)

if datetime.now() < quiz_open:
    st.warning("Check your time!")
    if st.button("Back to main page"):
        st.switch_page("app.py")
    st.stop()

if "step" not in st.session_state:
    st.session_state.step = 0
if "jeongdab" not in st.session_state:
    st.session_state.jeongdab = []

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

def questions(this_step, key, question):
    st.subheader("Pertanyaan")
    jeongdab = st.text_input(question, key=key)
    if st.button("Next", key=f"next_{key}"):
        if jeongdab.strip() == "":
            st.warning("Answer!")
        else:
            st.session_state.jeongdab.append((question, jeongdab.strip()))
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
    questions(0, "q1", "Pertanyaan 1")
elif step == 1:
    challenge(1, "c1", "Challenge 1")
elif step == 2:
    st.balloons()
    st.markdown(
        "<h3 style='text-align:center;'>Happy Anniversary, Bapak & Ibu! 💞</h3>",
        unsafe_allow_html=True,
    )
    if st.session_state.jeongdab:
        st.write("")
        st.subheader("Summary")
        for question, jeongdab in st.session_state.jawaban:
            st.markdown(f"**{question}**")
            st.write(jeongdab)
            st.write("")

        isi_txt = "\n\n".join(
            f"{question}\n{jeongdab}" for question, jeongdab in st.session_state.jeongdab
        )
        st.download_button(
            label="Download Jawaban (.txt)",
            data=isi_txt,
            file_name="jawaban_anniversary.txt",
            mime="text/plain",
        )
        st.caption("Jangan lupa klik download ditutup :))")
