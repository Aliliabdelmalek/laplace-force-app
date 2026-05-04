import streamlit as st
import pandas as pd
import math
from datetime import datetime

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="مختبر عليلي", layout="centered")

# تنسيق CSS مبسط جداً لضمان عدم التداخل على الهاتف
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; color: white !important; }
    .stApp { background-color: #0e1117; }
    h1 { color: #00d4ff !important; text-align: center; font-size: 1.5rem !important; }
    .main-box { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>🔬 مختبر عليلي الفيزيائي</h1>", unsafe_allow_html=True)
st.write(f"<p style='text-align:center;'>المبرمج: عبد المالك عليلي | {datetime.now().strftime('%Y-%m-%d')}</p>", unsafe_allow_html=True)

# القسم الرئيسي للحسابات
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.subheader("🎯 حساب قوة لابلاص")

I = st.number_input("التيار (I) بالأمبير:", value=2.0)
L = st.number_input("الطول (L) بالمتر:", value=0.5)
B = st.number_input("الحقل (B) بالتسلا:", value=0.1)
theta = st.slider("الزاوية (θ):", 0, 180, 90)

# معادلة الحساب
force = I * L * B * math.sin(math.radians(theta))

st.markdown(f"""
    <div style='background: #00d4ff; padding: 10px; border-radius: 5px; text-align: center; margin-top: 10px;'>
        <h2 style='color: black !important; margin: 0;'>F = {force:.4f} N</h2>
    </div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# اختبار بسيط
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.subheader("🧠 اختبار سريع")
q = st.radio("إذا كانت الزاوية 0، القوة تكون:", ["معدومة", "أعظمية"])
if st.button("تحقق من الإجابة"):
    if q == "معدومة":
        st.success("أحسنت! إجابة صحيحة")
        st.balloons()
    else:
        st.error("حاول مرة أخرى")
st.markdown('</div>', unsafe_allow_html=True)

# التواصل
st.markdown(f"""
    <div style='text-align: center; padding: 10px;'>
        <p>للتواصل: <a href='mailto:aliliabdou826@gmail.com' style='color: #00d4ff;'>aliliabdou826@gmail.com</a></p>
        <p>🇩🇿 ولاية سطيف | 2026</p>
    </div>
""", unsafe_allow_html=True)
