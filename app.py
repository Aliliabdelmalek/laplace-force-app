import streamlit as st
import math

# 1. إعدادات الصفحة
st.set_page_config(page_title="مختبر المسيلة الذكي", page_icon="🔬", layout="centered")

# 2. التنسيق الجمالي (Light Mode)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    .stApp { background-color: #fcfcfc; font-family: 'Cairo', sans-serif; direction: rtl; }
    .physics-card {
        background-color: #ffffff; padding: 20px; border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08); margin-bottom: 20px;
        border-right: 8px solid #2E7D32; color: #333;
    }
    .stTabs [data-baseweb="tab"] { font-weight: bold; padding: 10px 20px; }
    h1 { color: #2E7D32 !important; text-align: center; font-weight: 900; }
    h2 { color: #1565C0 !important; }
    .vector-result { font-size: 50px; text-align: center; background: #e3f2fd; border-radius: 15px; padding: 10px; border: 2px dashed #1565C0; }
    </style>
    """, unsafe_allow_html=True)

# 3. العنوان
st.markdown("<h1>🔬 مختبر عبد المالك عليلي للفيزياء</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>📍 ولاية المسيلة | خبير البرمجيات التعليمية</p>", unsafe_allow_html=True)

tab_theory, tab_calc, tab_smart_vector = st.tabs(["💡 قوانين المغناطيس", "🔢 حاسبة الشدة", "🤖 المستنتج الذكي"])

# --- التبويبة الأولى: قوانين المغناطيس والرسومات ---
with tab_theory:
    st.markdown("""
    <div class="physics-card">
        <h2>🧲 القوانين الأساسية للمغناطيس</h2>
        <p><b>1. قانون الحقل المغناطيسي (B):</b> يتولد حول الناقل المستقيم ويعطى بالعلاقة:</p>
        <p style="text-align:center; background:#f0f2f6; padding:10px; border-radius:10px;"><b>B = (2 × 10⁻⁷ × I) / d</b></p>
        <p><b>2. تدفق الحقل (Φ):</b> يعبر عن عدد خطوط الحقل التي تخترق سطحاً ما:</p>
        <p style="text-align:center; background:#f0f2f6; padding:10px; border-radius:10px;"><b>Φ = B × S × cos(θ)</b></p>
    </div>
    <div class="physics-card" style="border-right-color: #FF9800;">
        <h2>🎨 توضيح كرتوني للمغناطيس</h2>
        <p>تخرج خطوط الحقل دائماً من القطب الشمالي (N) وتدخل في القطب الجنوبي (S).</p>
        <div style="text-align:center; font-size:60px;">🧲</div>
        <p style="text-align:center;">🔴 (N) >>>>>>>> 🔵 (S)</p>
    </div>
    """, unsafe_allow_html=True)

# --- التبويبة الثانية: حاسبة الشدة ---
with tab_calc:
    st.markdown("## 🔢 حساب شدة قوة لابلاص")
    I_val = st.number_input("التيار I (A):", value=2.0)
    L_val = st.number_input("الطول L (m):", value=0.5)
    B_val = st.number_input("الحقل B (T):", value=0.1)
    angle = st.slider("الزاوية θ:", 0, 180, 90)
    
    res = I_val * L_val * B_val * math.sin(math.radians(angle))
    st.success(f"الشدة المستنتجة: {res:.4f} نيوتن")

# --- التبويبة الثالثة: المستنتج الذكي للجهة ---
with tab_smart_vector:
    st.markdown("## 🤖 المستنتج الذكي لجهة القوة")
    st.write("اختر أوضاع اليد اليمنى وسأخبرك بجهة السهم:")
    
    col_i, col_b = st.columns(2)
    with col_i:
        dir_i = st.selectbox("جهة التيار (الإبهام):", ["للأعلى ⬆️", "للأسفل ⬇️", "لليمين ➡️", "لليسار ⬅️"])
    with col_b:
        dir_b = st.selectbox("جهة الحقل (السبابة):", ["نحو الناظر 🔵", "بعيداً عن الناظر ✖️"])

    # منطق المستنتج الذكي (تبسيط لقاعدة اليد اليمنى)
    st.write("### النتيجة المتوقعة لجهة القوة (F):")
    if "للأعلى" in dir_i and "بعيداً" in dir_b:
        st.markdown('<div class="vector-result">⬅️ (نحو اليسار)</div>', unsafe_allow_html=True)
    elif "للأعلى" in dir_i and "نحو الناظر" in dir_b:
        st.markdown('<div class="vector-result">➡️ (نحو اليمين)</div>', unsafe_allow_html=True)
    elif "لليمين" in dir_i and "بعيداً" in dir_b:
        st.markdown('<div class="vector-result">⬆️ (نحو الأعلى)</div>', unsafe_allow_html=True)
    elif "لليمين" in dir_i and "نحو الناظر" in dir_b:
        st.markdown('<div class="vector-result">⬇️ (نحو الأسفل)</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="vector-result">🔘 (تغير الوضعية للاستنتاج)</div>', unsafe_allow_html=True)
 st.info("ملاحظة: هذا المستنتج يعتمد خوارزمية قاعدة اليد اليمنى لتمثيل الحركة ميكانيكياً.")

# 5. التوقيع
st.markdown("---")
st.markdown(f"""
<div style="text-align:center; background: #2E7D32; color:white; padding:15px; border-radius:15px;">
    <h3 style="color:white !important; margin:0;">إبداع المبرمج عبد المالك عليلي 🇩🇿</h3>
    <p>ولاية المسيلة | 2026</p>
</div>
""", unsafe_allow_html=True)
st.balloons()
