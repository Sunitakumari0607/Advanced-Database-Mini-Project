import streamlit as st
import time

st.set_page_config(page_title="SQLMorph", layout="centered")

# -------------------- THEME --------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* Glass Card */
.glass {
    background: rgba(255, 255, 255, 0.05);
    padding: 25px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    margin-top: 20px;
}

/* Title Animation */
.title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    animation: fadeIn 1.5s ease-in-out;
}

/* Fade Animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #6366f1, #3b82f6);
    color: white;
    border-radius: 10px;
    height: 45px;
    width: 100%;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- SOUND --------------------
st.markdown("""
<audio id="flip" src="https://www.soundjay.com/page-flip/page-flip-01a.mp3"></audio>
<script>
function playFlip(){
    document.getElementById("flip").play();
}
</script>
""", unsafe_allow_html=True)

# -------------------- TITLE --------------------
st.markdown('<div class="title">📘 SQLMorph</div>', unsafe_allow_html=True)

st.markdown("### Intelligent SQL Conversion System")

# -------------------- CONTENT --------------------
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.markdown("""
SQLMorph transforms Oracle SQL queries into PostgreSQL using intelligent retrieval-based techniques.
""")
st.markdown('</div>', unsafe_allow_html=True)

# FEATURES
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.markdown("### 🔥 Key Features")
st.markdown("""
- Feature-aware Top-K retrieval (RAG)  
- Weighted voting for accuracy  
- Confidence scoring  
- Rule-based fallback  
""")
st.markdown('</div>', unsafe_allow_html=True)

# TECH
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.markdown("### 🛠 Technologies")
st.markdown("""
Python • Streamlit • Retrieval-based AI
""")
st.markdown('</div>', unsafe_allow_html=True)

# USE CASE
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.markdown("### 🎯 Use Case")
st.markdown("Database migration from Oracle → PostgreSQL")
st.markdown('</div>', unsafe_allow_html=True)

# EXTRA FEATURES
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.markdown("### ⚡ Capabilities")
st.markdown("""
✔ RAG-based conversion  
✔ Confidence scoring  
✔ Error analysis  
""")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------- NAVIGATION --------------------
if st.button("🚀 Enter Converter"):
    st.markdown("<script>playFlip()</script>", unsafe_allow_html=True)

    with st.spinner("Loading Converter..."):
        time.sleep(2)

    st.switch_page("pages/1_Converter.py")