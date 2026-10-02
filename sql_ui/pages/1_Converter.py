import streamlit as st
from engine import convert

st.set_page_config(layout="wide")

# -------------------- STYLE --------------------
st.markdown("""
<style>
body {
    background-color: #020617;
}

/* Card */
.card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
}

/* Title */
.title {
    font-size: 30px;
    font-weight: bold;
}

/* Fade animation */
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

.fade {
    animation: fadeIn 1s;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title fade">🔄 SQL Converter</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

# ---------------- INPUT ----------------
with col1:
    st.markdown('<div class="card fade">', unsafe_allow_html=True)

    st.markdown("### 💡 Oracle Query")

    query = st.text_area("", height=200)

    st.markdown("### ⚡ Examples")

    examples = [
        "SELECT SYSDATE FROM dual;",
        "SELECT * FROM emp WHERE ROWNUM <= 5;",
        "BEGIN UPDATE emp SET salary=salary+100; END;",
        "SELECT * FROM emp WHERE salary > (SELECT AVG(salary) FROM emp);"
    ]

    selected = st.selectbox("Choose", ["None"] + examples)

    if selected != "None":
        query = selected

    btn = st.button("Convert")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- OUTPUT ----------------
with col2:
    st.markdown('<div class="card fade">', unsafe_allow_html=True)

    st.markdown("### 📤 Output")

    if btn and query:
        with st.spinner("Converting..."):
            result, confidence = convert(query)

        st.code(result, language="sql")

        # CONFIDENCE BAR
        st.markdown("### 📊 Confidence")

        st.progress(min(confidence,1.0))

        st.markdown(f"## {round(confidence*100)}%")

        if confidence > 0.75:
            st.success("High Confidence")
        elif confidence > 0.4:
            st.warning("Medium Confidence")
        else:
            st.error("Low Confidence")

    st.markdown('</div>', unsafe_allow_html=True)