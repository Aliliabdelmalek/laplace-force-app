import streamlit as st
import numpy as np

# إعدادات الصفحة
st.set_page_config(page_title="تطبيق عبد المالك الاحترافي", page_icon="⚡", layout="centered")

# --- زخرفة الواجهة باستخدام CSS المتقدم ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@900&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }

    .main-title {
        font-size: 50px !important;
        font-weight: 900 !important;
        background: linear-gradient(45deg, #FF0000, #FFD700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        text-shadow: 3px 3px 10px rgba(0,0,0,0.2);
        margin-bottom: 5px;
    }

    .dev-banner {
        background: linear-gradient(90deg, #1e1e2f, #2d3436);
        color: #00d2ff;
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        border: 2px solid #00d2ff;
        box-shadow: 0px 10px 30px rgba(0,210,255,0.3);
        font-size: 24px;
        font-weight: bold;
    }

    .stSelectbox label {
        font-size: 22px !important;
        font-weight: bold !important;
        color: #2d3436 !important;
    }

    .result-card {
        background: #ffffff;
        padding: 30px;
        border-radius: 25px;
        border-right: 15px solid #00c853;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        text-align: center;
        margin-top: 20px;
    }

    .result-text {
        font-size: 35px;
        font-weight: 900;
        color: #1b5e20;
    }

    /* زخرفة الأزرار */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #00d2ff, #3a7bd5);
        color: white;
        font-size: 25px !important;
        font-weight: 900 !important;
        height: 70px;
        border-radius: 20px;
        border: none;
        box-shadow: 0 5px 15px rgba(0,210,255,0.4);
        transition: 0.4s;
    }
    
    .stButton>button:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,210,255,0.6);
        color: #ffd700;
    }
    </style>
    """, unsafe_allow_html=True)

# --- محتوى الواجهة ---
st.markdown('<p class="main-title">⚡ مستكشف قوة لابلاص</p>', unsafe_allow_html=True)
st.markdown('<div class="dev-banner">🌟 المبرمج الرسمي: عبد المالك عليلي 🌟</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

directions = {
    "أعلى (↑)": [0, 1, 0], "أسفل (↓)": [0, -1, 0],
    "يمين (→)": [1, 0, 0], "يسار (←)": [-1, 0, 0],
    "خارج (⊙)": [0, 0, 1], "داخل (⊗)": [0, 0, -1]
}

col1, col2 = st.columns(2)
with col1:
    i_choice = st.selectbox("📌 جهة التيار (I):", list(directions.keys()))
with col2:
    b_choice = st.selectbox("نت جهة الحقل (B):", list(directions.keys()))

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 اضغط هنا لتحليل القوة"):
    v_i = np.array(directions[i_choice])
    v_b = np.array(directions[b_choice])
    v_f = np.cross(v_i, v_b)
    
    res = next((n for n, v in directions.items() if np.array_equal(v, v_f)), None)
    
    if res:
        st.balloons()
        st.markdown(f"""
            <div class="result-card">
                <p style="font-size: 20px; color: #666;">تم التحديد بنجاح ✅</p>
                <p class="result-text">جهة القوة هي: {res}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.error("⚠️ القوة معدومة (توازي المتجهات)")

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<center>حقوق البرمجة محفوظة © 2026 | عبد المالك عليلي</center>", unsafe_allow_html=True)