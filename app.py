import streamlit as st
import math

# 1. إعدادات الصفحة والاسم الأصلي
st.set_page_config(page_title="المختبر الفيزيائي الرقمي", page_icon="🚀", layout="centered")

# 2. إجبار الوضع الفاتح وتنسيق النصوص (ضد الوضع المظلم)
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
        text-align: center; font-weight: bold; color: #2E7D32 !important; font-size: 1.1rem;
    }
    .result-vector {
        font-size: 70px; text-align: center; background: #fff3e0; 
        border-radius: 20px; border: 3px solid #ff9800; padding: 20px; margin-top: 10px;
    }
    h1 { color: #2E7D32 !important; text-align: center; font-weight: 900; }
    label { color: #000000 !important; font-weight: bold !important; font-size: 1.1rem !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>🚀 المختبر الفيزيائي الرقمي</h1>", unsafe_allow_html=True)

tab_calc, tab_terms, tab_smart, tab_contact = st.tabs(["🔢 حاسبة لابلاص", "📚 قاموس المصطلحات", "🤖 المستنتج الذكي", "📧 تواصل معي"])

# --- التبويبة 1: الحاسبة ---
with tab_calc:
    st.markdown('<div class="physics-card">', unsafe_allow_html=True)
    I = st.number_input("شدة التيار I (أمبير):", value=2.0)
    L = st.number_input("طول الناقل L (متر):", value=0.5)
    B = st.number_input("شدة الحقل B (تسلا):", value=0.1)
    theta = st.number_input("الزاوية θ (درجة):", 0, 180, 90)
    F = I * L * B * math.sin(math.radians(theta))
    st.markdown(f"<div class='law-box'>النتيجة النهائية: F = {F:.4f} Newton</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- التبويبة 2: 15 مصطلح وقانون كاملة ---
with tab_terms:
    st.markdown("## 📚 القاموس الفيزيائي الشامل (15)")
    c1, c2 = st.columns(2)
    t_list = [
        ("قوة لابلاص", "F = I.L.B.sin(θ)"), ("شدة الحقل (B)", "وحدتها التسلا (T)"),
        ("التيار (I)", "تدفق شحنات (A)"), ("قانون أوم", "U = R . I"),
        ("الوشيعة", "ناقل ملفوف حلزونياً"), ("المغناطيس", "قطبان N و S"),
        ("التواتر (f)", "عدد الدورات (Hz)"), ("الدور (T)", "T = 1/f"),
        ("الاستطاعة", "P = U . I (W)"), ("خطوط الحقل", "من القطب N إلى S"),
        ("النفاذية", "قدرة الوسط المغناطيسية"), ("المحرض", "مصدر الحقل"),
        ("المتحرض", "مولد التيار"), ("تيار AC", "متغير الشدة والجهة"),
        ("الفعل المتبادل", "تأثير مغناطيس على تيار")
    ]
    for i, (name, law) in enumerate(t_list):
        col = c1 if i < 8 else c2
        col.markdown(f'<div class="physics-card"><b>{name}</b><div class="law-box">{law}</div></div>', unsafe_allow_html=True)

# --- التبويبة 3: المستنتج الذكي (تصحيح النتيجة) ---
with tab_smart:
    st.subheader("🤖 مستنتج جهة القوة (النتيجة)")
    i_d = st.selectbox("جهة التيار (الإبهام):", ["للأعلى ⬆️", "للأسفل ⬇️", "لليمين ➡️", "لليسار ⬅️"])
    b_d = st.selectbox("جهة الحقل (السبابة):", ["نحو الناظر (نقطة) 🔵", "بعيداً عن الناظر (✖️)"])
    
    # خوارزمية تحديد النتيجة
    res_icon, res_text = "🔘", "حدد المعطيات"
    if "للأعلى" in i_d and "بعيداً" in b_d: res_icon, res_text = "⬅️", "نحو اليسار"
    elif "للأعلى" in i_d and "نحو الناظر" in b_d: res_icon, res_text = "➡️", "نحو اليمين"
    elif "لليمين" in i_dir if 'i_dir' in locals() else "لليمين" in i_d and "بعيداً" in b_d: res_icon, res_text = "⬆️", "نحو الأعلى"
    elif "لليمين" in i_d and "نحو الناظر" in b_d: res_icon, res_text = "⬇️", "نحو الأسفل"

    # عرض النتيجة بشكل ضخم وواضح
    st.markdown(f"""
    <div class="result-vector">
        {res_icon}<br>
        <span style="font-size:22px; color:#333;">جهة القوة الناتجة هي: <b>{res_text}</b></span>
    </div>
    """, unsafe_allow_html=True)
# --- التبويبة 4: التواصل ---
with tab_contact:
    st.markdown(f'<div class="physics-card" style="text-align:center;"><h3>📧 تواصل معي</h3><b>عبد المالك عليلي</b><br>aliliabdou826@gmail.com<br>📍 ولاية المسيلة</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align:center;'>حقوق البرمجية محفوظة للمبدع عبد المالك عليلي 🇩🇿</p>", unsafe_allow_html=True)
st.balloons()
