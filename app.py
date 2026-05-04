import streamlit as st
import math

# 1. إعدادات الصفحة
st.set_page_config(page_title="المختبر الفيزيائي الرقمي", page_icon="🚀", layout="centered")

# 2. إجبار الوضع الفاتح (ضد الوضع المظلم)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    .stApp { background-color: #ffffff !important; color: #000000 !important; font-family: 'Cairo', sans-serif; direction: rtl; }
    .physics-card {
        background-color: #f8f9fa !important; padding: 15px; border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin-bottom: 15px;
        border-right: 6px solid #2E7D32; color: #000000 !important;
    }
    .law-box {
        background: #e8f5e9 !important; padding: 8px; border-radius: 8px;
        text-align: center; font-weight: bold; color: #2E7D32 !important;
    }
    h1 { color: #2E7D32 !important; text-align: center; font-weight: 900; }
    label { color: #000000 !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

# العودة للاسم الأصلي
st.markdown("<h1>🚀 المختبر الفيزيائي الرقمي</h1>", unsafe_allow_html=True)

tab_calc, tab_terms, tab_smart, tab_contact = st.tabs(["🔢 حاسبة لابلاص", "📚 قاموس المصطلحات", "🤖 المستنتج الذكي", "📧 تواصل معي"])

with tab_calc:
    st.markdown('<div class="physics-card">', unsafe_allow_html=True)
    st.subheader("🔢 حساب شدة قوة لابلاص")
    I = st.number_input("شدة التيار I (أمبير):", value=2.0)
    L = st.number_input("طول الناقل L (متر):", value=0.5)
    B = st.number_input("شدة الحقل B (تسلا):", value=0.1)
    theta = st.number_input("الزاوية θ (درجة):", 0, 180, 90)
    F = I * L * B * math.sin(math.radians(theta))
    st.markdown(f"<div class='law-box'>النتيجة: F = {F:.4f} Newton</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab_terms:
    st.markdown("## 📚 القاموس الفيزيائي المعتمد")
    c1, c2 = st.columns(2)
    t_list = [
        ("قوة لابلاص", "F = I.L.B.sin(θ)"), ("شدة الحقل", "تقاس بالتسلا (T)"),
        ("التيار (I)", "تدفق شحنات (A)"), ("قانون أوم", "U = R . I"),
        ("الوشيعة", "ناقل ملفوف حلزونياً"), ("المغناطيس", "له قطبان N و S"),
        ("التواتر (f)", "يحسب بالهرتز (Hz)"), ("الدور (T)", "T = 1/f"),
        ("الاستطاعة", "P = U . I (W)"), ("خطوط الحقل", "تتجه من N إلى S"),
        ("النفاذية", "قدرة الوسط المغناطيسية"), ("المحرض", "مصدر الحقل"),
        ("المتحرض", "الذي يتولد فيه التيار"), ("تيار AC", "تيار متغير الجهة"),
        ("الفعل المتبادل", "تأثير مغناطيس على تيار")
    ]
    for i, (name, law) in enumerate(t_list):
        target_col = c1 if i < 8 else c2
        target_col.markdown(f'<div class="physics-card"><b>{name}</b><div class="law-box">{law}</div></div>', unsafe_allow_html=True)

with tab_smart:
    st.subheader("🤖 مستنتج جهة القوة")
    i_d = st.selectbox("جهة التيار:", ["للأعلى ⬆️", "للأسفل ⬇️", "لليمين ➡️", "لليسار ⬅️"])
    b_d = st.selectbox("جهة الحقل (السبابة):", ["نحو الناظر (نقطة) 🔵", "بعيداً عن الناظر (✖️)"])
    st.info("استخدم قاعدة اليد اليمنى للتأكد")

with tab_contact:
    st.markdown("""
    <div class="physics-card" style="text-align:center;">
        <h3>📧 مركز التواصل المباشر</h3>
        <p>المبرمج: <b>عبد المالك عليلي</b></p>
        <p style="color:#1565C0;">aliliabdou826@gmail.com</p>
        <p>📍 ولاية المسيلة | الجزائر</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align:center;'>حقوق البرمجية محفوظة للمبدع عبد المالك عليلي 🇩🇿</p>", unsafe_allow_html=True)
