import streamlit as st
import math

# 1. إعدادات الصفحة
st.set_page_config(page_title="مختبر عبد المالك الفيزيائي", page_icon="🔬", layout="centered")

# 2. تنسيق الواجهة الفاتحة (Light Theme) بنفس منهجيتنا الأخيرة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    .stApp {
        background-color: #fcfcfc;
        font-family: 'Cairo', sans-serif;
        direction: rtl;
    }
    
    /* تنسيق البطاقات التعليمية */
    .physics-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        border-right: 8px solid #2E7D32;
        color: #333;
    }
    
    /* تنسيق التبويبات (Tabs) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #f0f2f6;
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        color: #333 !important;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] {
        background-color: #2E7D32 !important;
        color: white !important;
    }

    h1 { color: #2E7D32 !important; text-align: center; font-weight: 900; font-size: 2rem !important; }
    h2 { color: #1565C0 !important; font-size: 1.3rem !important; }
    .highlight { color: #d32f2f; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. رأس الصفحة (العالم أينشتاين والذرة)
st.markdown("<h1>🔬 موسوعة قوة لابلاص الرقمية</h1>", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; margin-bottom: 20px;">
    <span style="font-size:60px;">👨‍🔬</span> <span style="font-size:40px;">⚛️</span>
    <p style="color:#666;">بإشراف المبرمج: <b>عبد المالك عليلي</b> (المسيلة)</p>
</div>
""", unsafe_allow_html=True)

# 4. نظام التبويبات المنظم
tab_theory, tab_calc, tab_direction = st.tabs(["💡 عن القوة", "🔢 حاسبة القوة", "🖐️ جهة القوة"])

# --- التبويبة الأولى: شرح فيزيائي كرتوني ---
with tab_theory:
    st.markdown("""
    <div class="physics-card">
        <h2>👨‍🏫 ما هي قوة لابلاص؟</h2>
        <p>هي القوة التي يمارسها حقل مغناطيسي على سلك يمر به تيار كهربائي. تخيل أن الكهرباء والمغناطيس يتحدان لتحريك الأشياء!</p>
        <div style="text-align:center; font-size:50px;">🧲 + ⚡ = 🏃</div>
    </div>
    <div class="physics-card" style="border-right-color: #FF9800;">
        <h2>⚛️ سر الذرة</h2>
        <p>الإلكترونات الصغيرة داخل السلك هي التي تخلق هذا السحر الفيزيائي عند حركتها.</p>
        <div style="text-align:center; font-size:40px;">🌀✨</div>
    </div>
    """, unsafe_allow_html=True)

# --- التبويبة الثانية: حاسبة قوة لابلاص (إعادة الحسابات) ---
with tab_calc:
    st.markdown('<div class="physics-card" style="border-right-color: #1565C0;">', unsafe_allow_html=True)
    st.markdown("<h2>🔢 استنتاج شدة القوة</h2>", unsafe_allow_html=True)
    
    # مدخلات الحساب
    I = st.number_input("شدة التيار I (أمبير):", value=2.0)
    L = st.number_input("طول السلك L (متر):", value=0.5)
    B = st.number_input("الحقل المغناطيسي B (تسلا):", value=0.1)
    theta = st.slider("الزاوية (درجة):", 0, 180, 90)
    
    # عملية الحساب
    force = I * L * B * math.sin(math.radians(theta))
    
    # عرض النتيجة بشكل مبهج
    st.markdown(f"""
    <div style='background: #e3f2fd; padding: 15px; border-radius: 10px; text-align: center; border: 2px solid #1565C0;'>
        <p style='color: #1565C0; margin:0;'>الشدة الناتجة F هي:</p>
        <h2 style='color: #d32f2f !important; font-size: 30px !important; margin: 5px 0;'>{force:.4f} Newton</h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- التبويبة الثالثة: استنتاج جهة القوة ---
with tab_direction:
    st.markdown("""
[04-05-2026 15:31] Abdou Trader: <div class="physics-card" style="border-right-color: #E91E63;">
        <h2>👋 قاعدة اليد اليمنى</h2>
        <p>استخدم أصابع يدك اليمنى لتحديد جهة الحركة:</p>
        <ul>
            <li>🚩 <b>الإبهام:</b> يشير إلى جهة التيار الكهربائي.</li>
            <li>🧲 <b>السبابة:</b> تشير إلى جهة الحقل المغناطيسي.</li>
            <li>🏹 <b>الوسطى:</b> تشير إلى جهة القوة الناتجة.</li>
        </ul>
        <div style="text-align:center; font-size:50px;">🖐️ 📐 ✨</div>
    </div>
    """, unsafe_allow_html=True)

# 5. التذييل المسيلي الأنيق
st.markdown("---")
st.markdown(f"""
<div style="text-align:center; background: linear-gradient(to right, #1b5e20, #2E7D32); color:white; padding:20px; border-radius:15px;">
    <h3 style="color:white !important; margin:0;">تم التطوير بكل فخر في ولاية المسيلة الأبية 🇩🇿</h3>
    <p style="margin:5px 0;">المبرمج: <b>عبد المالك عليلي</b></p>
    <p style="font-size:12px;">مختبر الفيزياء الذكي | 2026</p>
</div>
""", unsafe_allow_html=True)

st.balloons()
