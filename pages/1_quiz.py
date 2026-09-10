import streamlit as st
from datetime import date, datetime

quiz_open = datetime(2026, 9, 10, 13, 24)

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
    questions(0, "q1", "Di mana lokasi bapak ibu pertama kali nge-date?")
elif step == 1:
    questions(1, "q2", "Siapa yang paling banyak usaha pas masa PDKT, dan apa jurus utamanya?")
elif step == 2:
    questions(2, "q3", "Apa barang pertama yang pernah diberikan masing-masing waktu masih pacaran?")
elif step == 3:
    challenge(3, "c1", "Ceritakan kembali momen paling konyol atau bikin malu pas masa-masa awal pacaran/pernikahan")
elif step == 4:
    questions(4, "q4", "Lagu apa yang paling identik dengan masa pacaran bapak ibu?")
elif step == 5:
    questions(5, "q5", "Apa yang pertama kali bikin bapak ibu tertarik satu sama lain?")
elif step == 6:
    questions(6, "q6", "Apa yang paling diingat dari hari pernikahan bapak ibu?")
elif step == 7:
    challenge(7, "c2", "Pelukan erat-erat selama 15 detik tanpa boleh lepas")
elif step == 8:
    questions(8, "q7", "Makanan apa yang selalu mengingatkan pada kenangan tertentu?")
elif step == 9:
    questions(9, "q8", "Tempat mana yang paling ingin dikunjungi lagi bersama, kenapa?")
elif step == 10:
    challenge(10, "c3", "Bisikkan 3 hal kecil dari pasangan yang paling disyukuri selama puluhan tahun hidup bareng")
elif step == 11:
    questions(11, "q9", "Apa harapan untuk perjalanan ke depan bersama?")
elif step == 12:
    st.balloons()
    st.markdown(
        "<h3 style='text-align:center;'>Happy Anniversary, Bapak Ibu! 💞</h3>",
        unsafe_allow_html=True,
    )
    if st.session_state.jeongdab:
        st.write("")
        st.subheader("Summary")
        for question, jeongdab in st.session_state.jeongdab:
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
        st.caption("Jangan lupa klik download sebelum ditutup :)")
        st.caption("(buat save doang)")
