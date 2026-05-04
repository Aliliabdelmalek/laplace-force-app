import streamlit as st
import math

# 1. إعدادات الصفحة الأساسية بالاسم الذي تفضله
st.set_page_config(page_title="المختبر الفيزيائي الرقمي", page_icon="🚀", layout="centered")

# 2. التعليمة البرمجية لإجبار الوضع الفاتح ومنع الوضع المظلم نهائياً
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* إجبار الخلفية والنصوص على البقاء في الوضع الفاتح */
    .stApp {
        background-color: #ffffff !important;
        color: #000000 !important;
        font-family: 'Cairo', sans-serif;
        direction: rtl;
    }

    /* تنسيق البطاقات والمربعات لضمان الوضوح */
    .physics-card {
        background-color: #f8f9fa !important;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 15px;
        border-right: 6px solid #2E7D32;
        color: #000000 !important;
    }

    .law-box {
        background: #e8f5e9 !important;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        color: #2E7D32 !important;
        border: 1px solid #c8e6c9;
    }

    /* ضمان ظهور أسماء التبويبات باللون الأسود */
    .stTabs [data-baseweb="tab"] p {
        color: #000000 !important;
        font-weight: bold;
    }
    
    h1, h2, h3 { color: #2E7D32 !important; text-align: center; font-weight: 900; }
    label { color: #000000 !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown("<h1>🚀 المختبر الفيزيائي الرقمي</h1>", unsafe_allow_html=True)

# تقسيم التطبيق إلى تبويبات واضحة
tab_calc, tab_terms, tab_smart, tab_contact = st.tabs(["🔢 حاسبة لابلاص", "📚 قاموس المصطلحات", "🤖 المستنتج الذكي", "📧 تواصل معي"])

# --- التبويبة الأولى: الحاسبة ---
with tab_calc:
    st.markdown('<div class="physics-card">', unsafe_allow_html=True)
    st.subheader("🔢 حساب شدة قوة لابلاص")
    I = st.number_input("شدة التيار I (أمبير):", value=2.0)
    L = st.number_input("طول الناقل L (متر):", value=0.5)
    B = st.number_input("شدة الحقل B (تسلا):", value=0.1)
    theta = st.number_input("الزاوية θ (بالدرجات):", 0, 180, 90)
    
    # حساب النتيجة
    F = I * L * B * math.sin(math.radians(theta))
    st.markdown(f"<div class='law-box'>النتيجة النهائية: F = {F:.4f} Newton</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- التبويبة الثانية: القاموس (15 مصطلح وقانون) ---
with tab_terms:
    st.markdown("## 📚 القاموس الفيزيائي الشامل")
    c1, c2 = st.columns(2)
    terms = [
        ("قوة لابلاص", "F = I.L.B.sin(θ)"), ("شدة الحقل", "تقاس بالتسلا (T)"),
        ("التيار (I)", "شحنات كهربائية (A)"), ("قانون أوم", "U = R . I"),
        ("الوشيعة", "سلك ملفوف حلزونياً"), ("المغناطيس", "قطبان شمالي وجنوبي"),
        ("التواتر (f)", "الهرتز (Hz)"), ("الدور (T)", "T = 1/f"),
        ("الاستطاعة", "P = U . I (W)"), ("خطوط الحقل", "تتجه من N إلى S"),
        ("النفاذية", "الاستجابة المغناطيسية"), ("المحرض", "مصدر الحقل المغناطيسي"),
        ("المتحرض", "العنصر الذي يولد التيار"), ("تيار AC", "متناوب الشدة والجهة"),
        ("الفعل المتبادل", "التأثير بين المغناطيس والتيار")
    ]
    for i, (name, law) in enumerate(terms):
        target_col = c1 if i < 8 else c2
        target_col.markdown(f'<div class="physics-card"><b>{name}</b><div class="law-box">{law}</div></div>', unsafe_allow_html=True)

# --- التبويبة الثالثة: المستنتج الذكي ---
with tab_smart:
    st.subheader("🤖 مستنتج جهة القوة")
    i_dir = st.selectbox("جهة التيار:", ["للأعلى ⬆️", "للأسفل ⬇️", "لليمين ➡️", "لليسار ⬅️"])
    b_dir = st.selectbox("جهة الحقل:", ["نحو الناظر (🔵)", "بعيداً عن الناظر (✖️)"])
    
    # خوارزمية النتيجة
    res_icon, res_text = "🔘", "بانتظار المعطيات"
    if "للأعلى" in i_dir and "بعيداً" in b_dir: res_icon, res_text = "⬅️", "نحو اليسار"
    elif "للأعلى" in i_dir and "نحو الناظر" in b_dir: res_icon, res_text = "➡️", "نحو اليمين"
    elif "لليمين" in i_dir and "بعيداً" in b_dir: res_icon, res_text = "⬆️", "نحو الأعلى"
    elif "لليمين" in i_dir and "نحو الناظر" in b_dir: res_icon, res_text = "⬇️", "نحو الأسفل"

    st.markdown(f'<div class="law-box" style="font-size:30px;">{res_icon}<br>{res_text}</div>', unsafe_allow_html=True)

# --- التبويبة الرابعة: التواصل ---
with tab_contact:
    st.markdown(f'<div class="physics-card" style="text-align:center;"><h3>📧 مركز التواصل المباشر</h3>المبرمج: <b>عبد المالك عليلي</b><br>aliliabdou826@gmail.com<br>📍 ولاية المسيلة | الجزائر</div>', unsafe_allow_html=True)

# التذييل
st.markdown("---")
st.markdown("<p style='text-align:center;'>حقوق الملكية محفوظة للمبدع عبد المالك عليلي © 2026</p>", unsafe_allow_html=True)
st.balloons()
