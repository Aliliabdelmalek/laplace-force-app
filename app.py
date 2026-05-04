import streamlit as st
import math

# 1. إعدادات الصفحة
st.set_page_config(page_title="موسوعة عبد المالك الفيزيائية", page_icon="⚛️", layout="centered")

# 2. التنسيق الجمالي (Light Mode) المحسن
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    .stApp { background-color: #fcfcfc; font-family: 'Cairo', sans-serif; direction: rtl; }
    .physics-card {
        background-color: #ffffff; padding: 15px; border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06); margin-bottom: 15px;
        border-right: 6px solid #2E7D32; color: #333;
    }
    .law-box { background: #f1f8e9; padding: 8px; border-radius: 8px; border: 1px solid #c8e6c9; text-align: center; font-weight: bold; margin: 5px 0; }
    .term-title { color: #1565C0; font-weight: bold; font-size: 1.1rem; }
    h1 { color: #2E7D32 !important; text-align: center; font-weight: 900; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>🔬 مختبر المسيلة الشامل للفيزياء</h1>", unsafe_allow_html=True)

tab_calc, tab_terms, tab_smart, tab_contact = st.tabs(["🔢 حاسبة لابلاص", "📚 قاموس المصطلحات", "🤖 المستنتج الذكي", "📧 تواصل معي"])

# --- التبويبة الأولى: الحاسبة (مع حل مشكلة الزاوية) ---
with tab_calc:
    st.subheader("🔢 حساب شدة قوة لابلاص")
    I = st.number_input("شدة التيار I (A):", value=2.0)
    L = st.number_input("طول الناقل L (m):", value=0.5)
    B = st.number_input("شدة الحقل B (T):", value=0.1)
    theta = st.number_input("الزاوية θ (بالدرجات):", 0, 180, 90)
    
    F = I * L * B * math.sin(math.radians(theta))
    st.success(f"النتيجة النهائية: F = {F:.4f} Newton")

# --- التبويبة الثانية: 15 مصطلح وقانون (جديد) ---
with tab_terms:
    st.markdown("## 📚 أهم 15 مصطلح وقانون فيزيائي")
    
    col1, col2 = st.columns(2)
    
    with col1:
        terms_1 = [
            ("قوة لابلاص (F)", "F = I . L . B . sin(θ)"),
            ("شدة الحقل (B)", "تقاس بوحدة التسلا (T)"),
            ("التيار الكهربائي (I)", "تدفق الإلكترونات، يقاس بالأمبير (A)"),
            ("الناقل المستقيم", "سلك يسمح بمرور التيار وتوليد حقل"),
            ("النفاذية المغناطيسية", "قدرة الوسط على تمرير خطوط الحقل"),
            ("المغناطيس الدائم", "جسم يملك قطبين (N) و (S) ثابتين"),
            ("الوشيعة المسطحة", "ناقل ملفوف يولد حقل مغناطيسي مركز"),
            ("قانون أوم", "U = R . I (العلاقة بين التوتر والتيار)")
        ]
        for title, law in terms_1:
            st.markdown(f'<div class="physics-card"><span class="term-title">{title}</span><div class="law-box">{law}</div></div>', unsafe_allow_html=True)

    with col2:
        terms_2 = [
            ("الحقل المغناطيسي الأرضي", "يحمي الأرض من الرياح الشمسية"),
            ("الفعل المتبادل", "التأثير المتبادل بين المغناطيس والتيار"),
            ("خطوط الحقل", "خطوط وهمية تخرج من N وتدخل في S"),
            ("المحرض (Inductor)", "العنصر الذي يولد الحقل (المغناطيس)"),
            ("المتحرض", "العنصر الذي يخضع للحقل (الوشيعة)"),
            ("التيار المتناوب (AC)", "تيار يتغير اتجاهه وشدته بانتظام"),
            ("التواتر (Frequency)", "عدد الدورات في الثانية، يقاس بالهرتز (Hz)"),
            ("الاستطاعة الكهربائية", "P = U . I (تقاس بالواط W)")
        ]
        for title, law in terms_2:
            st.markdown(f'<div class="physics-card"><span class="term-title">{title}</span><div class="law-box">{law}</div></div>', unsafe_allow_html=True)

# --- التبويبة الثالثة: المستنتج الذكي ---
with tab_smart:
    st.subheader("🤖 تحديد جهة القوة")
    i_dir = st.selectbox("جهة التيار:", ["للأعلى ⬆️", "للأسفل ⬇️", "لليمين ➡️", "لليسار ⬅️"])
    b_dir = st.selectbox("جهة الحقل:", ["نحو الناظر (نقطة) 🔵", "بعيداً عن الناظر (كروس) ✖️"])
    
    res_icon, res_text = "🔘", "انتظار المعطيات"
    if "للأعلى" in i_dir and "بعيداً" in b_dir: res_icon, res_text = "⬅️", "نحو اليسار"
    elif "للأعلى" in i_dir and "نحو الناظر" in b_dir: res_icon, res_text = "➡️", "نحو اليمين"
    elif "لليمين" in i_dir and "بعيداً" in b_dir: res_icon, res_text = "⬆️", "نحو الأعلى"
    elif "لليمين" in i_dir and "نحو الناظر" in b_dir: res_icon, res_text = "⬇️", "نحو الأسفل"

    st.markdown(f'<div style="font-size:60px; text-align:center;">{res_icon}<br><p style="font-size:20px;">الجهة: {res_text}</p></div>', unsafe_allow_html=True)

# --- التبويبة الرابعة: التواصل ---
with tab_contact:
    st.markdown("""
    <div class="physics-card" style="text-align:center; border-right-color: #1565C0;">
        <h2>📧 تواصل مع المبرمج</h2>
        <p>عبد المالك عليلي - ولاية المسيلة</p>
        <p style="font-size: 20px; color: #1565C0;"><b>aliliabdou826@gmail.com</b></p>
        <p>نرحب بطلبات تعديل النسخ الخاصة</p>
    </div>
    """, unsafe_allow_html=True)

# 4. التذييل
st.markdown("---")
st.markdown("<p style='text-align:center;'>صنع بكل فخر بواسطة <b>عبد المالك عليلي</b> | الجزائر 🇩🇿</p>", unsafe_allow_html=True)
st.balloons()
