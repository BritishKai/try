import streamlit as st
from datetime import datetime, date
import streamlit.components.v1 as components

wedding_date = date(1999, 9, 11)
now = datetime.now()
quiz_open = datetime(2026, 9, 10, 11, 52)

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
    f"<h3 style='text-align:center;'>It's been <span style='color:#EB7D00;'>{year} years, {month} months, {days} days</span> together 🎉</h3>",
    unsafe_allow_html=True,
)

st.write("")
col1, col2, col3 = st.columns(3)
col1.metric("Total Hari", f"{total:,}")
col2.metric("Estimasi Makan Bareng", f"{total*3:,}")
col3.metric("Estimasi Peluk", f"{total*2:,}")

st.markdown("<div class='sub-title'>Message dari WG</div>", unsafe_allow_html=True)
st.markdown("<div class='big-title'>Happy 26th Anniversary Bapak & Ibu 𑣲⋆</div>", unsafe_allow_html=True)

@st.dialog("Before go to the next page...")
def popup():
    st.write("Check the box below")
    cb = st.checkbox("Ibu sama Bapak udah sebelahan")

    checked = cb

    if st.button("Go to the next page", disabled=not checked):
        st.switch_page("pages/1_quiz.py")

if now < quiz_open:
    st.markdown("<h4 style='text-align:center;'>The next page will be opened in:</h4>", unsafe_allow_html=True)
    target_iso = quiz_open.isoformat()
    countdown_html = f"""
    <div style="text-align:center; font-size:1.8rem; font-weight:bold; color:#ff4d6d; font-family:sans-serif;">
      <span id="countdown">Counting...</span>
    </div>
    <script>
    const target = new Date("{target_iso}").getTime();
    function updateCountdown() {{
        const now = new Date().getTime();
        const distance = target - now;
        if (distance <= 0) {{
            document.getElementById("countdown").innerHTML = "Waktunya sudah tiba! 🎉";
            clearInterval(timer);
            setTimeout(function() {{ window.parent.location.reload(); }}, 1200);
            return;
        }}
        const hari = Math.floor(distance / (1000*60*60*24));
        const jam = Math.floor((distance % (1000*60*60*24)) / (1000*60*60));
        const menit = Math.floor((distance % (1000*60*60)) / (1000*60));
        const detik = Math.floor((distance % (1000*60)) / 1000);
        document.getElementById("countdown").innerHTML =
            hari + " days : " + jam + " hours : " + menit + " minutes : " + detik + " seconds";
    }}
    const timer = setInterval(updateCountdown, 1000);
    updateCountdown();
    </script>
    """
    components.html(countdown_html, height=70)
    st.button("⋆｡°✩ The next page can't be opened yet ✩°｡⋆", disabled=True)
else:
    if st.button("⋆｡°✩ You can now go to the next page ✩°｡⋆"):
        popup()