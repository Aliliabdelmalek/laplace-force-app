import streamlit as st
import math

# إعدادات الصفحة
st.set_page_config(page_title="مختبر عبد المالك الذكي", page_icon="🔬", layout="centered")

# التنسيق الجمالي (Light Mode)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    .stApp { background-color: #fcfcfc; font-family: 'Cairo', sans-serif; direction: rtl; }
    .physics-card {
        background-color: #ffffff; padding: 20px; border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08); margin-bottom: 20px;
        border-right: 8px solid #2E7D32; color: #333;
    }
    .vector-result { font-size: 60px; text-align: center; background: #f0f4f8; border-radius: 15px; padding: 20px; border: 3px solid #2E7D32; }
    h1 { color: #2E7D32 !important; text-align: center; font-weight: 900; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>🔬 مختبر المسيلة للفيزياء الرقمية</h1>", unsafe_allow_html=True)

tab_theory, tab_calc, tab_smart = st.tabs(["💡 قوانين المغناطيس", "🔢 حاسبة الشدة", "🤖 المستنتج الذكي"])

with tab_theory:
    st.markdown("""
    <div class="physics-card">
        <h2>🧲 قوانين هامة</h2>
        <p><b>قانون الحقل (B):</b> B = (2 × 10⁻⁷ × I) / d</p>
        <p><b>قانون التدفق (Φ):</b> Φ = B × S × cos(θ)</p>
        <div style="text-align:center; font-size:50px;">🧲</div>
    </div>
    """, unsafe_allow_html=True)

with tab_calc:
    st.subheader("🔢 حساب شدة قوة لابلاص")
    I = st.number_input("التيار I (A):", value=2.0)
    L = st.number_input("الطول L (m):", value=0.5)
    B = st.number_input("الحقل B (T):", value=0.1)
    theta = st.slider("الزاوية:", 0, 180, 90)
    F = I * L * B * math.sin(math.radians(theta))
    st.success(f"النتيجة: {F:.4f} Newton")

with tab_smart:
    st.subheader("🤖 تحديد جهة القوة برمجياً")
    col1, col2 = st.columns(2)
    with col1:
        i_dir = st.selectbox("جهة التيار (الإبهام):", ["للأعلى ⬆️", "للأسفل ⬇️", "لليمين ➡️", "لليسار ⬅️"])
    with col2:
        b_dir = st.selectbox("جهة الحقل (السبابة):", ["نحو الناظر (نقطة) 🟢", "بعيداً عن الناظر (كروس) ✖️"])

    # خوارزمية الاستنتاج الذكي
    res_icon = "🔘"
    res_text = "غير محدد"

    if "للأعلى" in i_dir and "بعيداً" in b_dir:
        res_icon, res_text = "⬅️", "نحو اليسار"
    elif "للأعلى" in i_dir and "نحو الناظر" in b_dir:
        res_icon, res_text = "➡️", "نحو اليمين"
    elif "لليمين" in i_dir and "بعيداً" in b_dir:
        res_icon, res_text = "⬆️", "نحو الأعلى"
    elif "لليمين" in i_dir and "نحو الناظر" in b_dir:
        res_icon, res_text = "⬇️", "نحو الأسفل"

    st.markdown(f"""
    <div class="vector-result">
        {res_icon}<br>
        <span style="font-size:20px;">الجهة: {res_text}</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align:center;'>صنع بكل فخر بواسطة <b>عبد المالك عليلي</b> | المسيلة 🇩🇿</p>", unsafe_allow_html=True)
