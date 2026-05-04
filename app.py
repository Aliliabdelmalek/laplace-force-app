import streamlit as st
import numpy as np
import plotly.graph_objects as go
import math

# --- إعدادات الصفحة الاحترافية ---
st.set_page_config(page_title="مختبر عليلي الفيزيائي الشامل", layout="wide", page_icon="🧲")

# --- تنسيق CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }
    .stApp { background: linear-gradient(135deg, #0f2027, #203a43, #2c5364); color: white; }
    .main-header { background: rgba(255, 255, 255, 0.1); padding: 30px; border-radius: 20px; border: 1px solid #00d4ff; text-align: center; }
    .email-link { color: #00d4ff !important; font-weight: 900; text-decoration: none; font-size: 1.3rem; }
    </style>
    """, unsafe_allow_html=True)

# --- القائمة الجانبية ---
with st.sidebar:
    st.markdown("## ⚙️ مركز التحكم")
    page = st.radio("اختر القسم:", ["🏠 المختبر الرئيسي", "🌀 حاسبة الحقول (B)", "🧠 اختبار الذكاء", "📧 تواصل معي"])
    st.write("---")
    st.markdown(f"المبرمج: عبد المالك عليلي")
    st.markdown(f'<a href="mailto:aliliabdou826@gmail.com" class="email-link">📩 أرسل ملاحظة</a>', unsafe_allow_html=True)

# --- واجهة المختبر الرئيسي ---
if page == "🏠 المختبر الرئيسي":
    st.markdown('<div class="main-header"><h1>🔬 موسوعة المغناطيسية العالمية</h1><p>الإصدار النهائي المطور بواسطة عبد المالك عليلي</p></div>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1.5])
    with col1:
        st.subheader("🎯 حاسبة قوة لابلاص")
        I = st.number_input("شدة التيار I (A):", value=2.0)
        L = st.number_input("طول الناقل L (m):", value=0.5)
        B = st.number_input("شدة الحقل B (T):", value=0.1)
        theta = st.slider("الزاوية (θ) بالدرجات:", 0, 180, 90)
        force = I * L * B * math.sin(math.radians(theta))
        st.metric("القوة الناتجة F", f"{force:.4f} Newton")
    with col2:
        angles = np.linspace(0, 180, 100)
        forces = I * L * B * np.sin(np.radians(angles))
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=angles, y=forces, mode='lines', line=dict(color='#00d4ff', width=3)))
        fig.update_layout(template="plotly_dark", title="تغير القوة بتغير الزاوية")
        st.plotly_chart(fig, use_container_width=True)

# --- واجهة حاسبة الحقول ---
elif page == "🌀 حاسبة الحقول (B)":
    st.header("🌀 حساب شدة الحقل المغناطيسي")
    i1 = st.number_input("التيار I (A):", value=2.0)
    d1 = st.number_input("المسافة d (m):", value=0.02)
    st.info(f"النتيجة: B = {(2e-7 * i1 / d1):.2e} Tesla")

# --- واجهة الاختبار ---
elif page == "🧠 اختبار الذكاء":
    st.header("🧠 تحدي العباقرة")
    q = st.radio("إذا كانت الزاوية 0، كم تكون قوة لابلاص؟", ["أعظمية", "معدومة"])
    if st.button("تحقق"):
        if q == "معدومة": st.success("إجابة صحيحة!"); st.balloons()
        else: st.error("إجابة خاطئة!")

# --- واجهة التواصل ---
elif page == "📧 تواصل معي":
    st.markdown(f'<div style="text-align:center;"><h2>اتصل بي</h2><br><a href="mailto:aliliabdou826@gmail.com" class="email-link">aliliabdou826@gmail.com</a></div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<center>صُنع بكل فخر بواسطة عبد المالك عليلي | 🇩🇿 الجزائر 2026</center>", unsafe_allow_html=True)
