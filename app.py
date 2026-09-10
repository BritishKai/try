import streamlit as st
from datetime import datetime, date
from streamlit_autorefresh import st_autorefresh

wedding_date = date(1999, 9, 11)
quiz_open = datetime(2026, 9, 10, 13, 27)

st.set_page_config(
    page_title="𑣲⋆ 27th Anniversary",
    layout="centered"
)

st.markdown(
    """
    <style>
    .block-container {padding-top: 2rem; padding-bottom: 3rem; max-width: 640px;}
    div[data-testid="stMetric"] {
        background-color: #EB7D00;
        border-radius: 14px;
        padding: 10px 4px;
        text-align: center;
    }
    .big-title {text-align:center; font-size: 2rem; margin-bottom: 0;}
    .sub-title {text-align:center; color: #EB7D00; margin-top: 4px;}
    .stButton>button {
        width: 100%;
        padding: 0.9em;
        font-size: 1.05rem;
        border-radius: 14px;
        background-color: #2C5745;
        color: white;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='big-title'>♡ Bapak & Ibu ♡</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Happy 26th Anniversary</div>", unsafe_allow_html=True)
st.write("")

today = date.today()
total = (today - wedding_date).days
year = total // 365
remaining = total % 365
month = remaining // 30
days = month % 30

st.markdown(
    f"<h3 style='text-align:center;'><span style='color:#EB7D00;'>{year} years together 🎉</h3>",
    unsafe_allow_html=True,
)

st.write("")
col1, col2, col3 = st.columns(3)
col1.metric("Total Hari", f"{total:,}")
col2.metric("Estimasi Makan Bareng", f"{total*3:,}")
col3.metric("Estimasi Peluk", f"{total*2:,}")

st.markdown("<div class='sub-title'>Message dari WG</div>", unsafe_allow_html=True)
st.markdown("<div class='big-title'>Happy 26th Anniversary Bapak & Ibu 𑣲⋆</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Widi Gegi bersyukur udah lahir dan terpilih buat jadi anaknya ibu sama bapak. Makasih ibu sama bapak udah rawat kita sampe sekarang. Kita berdoa terus supaya ibu sama bapak panjang umur, sehat selalu, bahagia selalu, dan bareng-bareng terus selama lama lama lamanya.</div>", unsafe_allow_html=True)

@st.dialog("Before go to the next page...")
def popup():
    st.write("Check the box below")
    cb = st.checkbox("Ibu sama Bapak udah sebelahan")

    checked = cb

    if st.button("Go to the next page", disabled=not checked):
        st.switch_page("pages/1_quiz.py")

now = datetime.now()

if now < quiz_open:
    st_autorefresh(interval=1000, key="countdown_tick")  # rerun tiap 1 detik

    sisa = quiz_open - now
    hari = sisa.days
    jam, sisa_detik = divmod(sisa.seconds, 3600)
    menit, detik = divmod(sisa_detik, 60)

    st.markdown("<h4 style='text-align:center;'>The next page will be opened in:</h4>", unsafe_allow_html=True)
    st.markdown(
        f"<div style='text-align:center; font-size:1.8rem; font-weight:bold; color:#ff4d6d;'>"
        f"{hari} days : {jam} hours : {menit} minutes : {detik} seconds</div>",
        unsafe_allow_html=True,
    )
    st.button("⋆｡°✩ The next page can't be opened yet ✩°｡⋆", disabled=True)
else:
    if st.button("⋆｡°✩ You can now go to the next page ✩°｡⋆"):
        popup()
