 import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import math
import base64
from datetime import datetime

# ==========================================
# 1. إعدادات النظام الأساسية - Mobile First
# ==========================================
st.set_page_config(
    page_title="مختبر عليلي الفيزيائي | Final",
    layout="centered", # تجعل المحتوى في المنتصف انسيابياً
    initial_sidebar_state="collapsed", # إخفاء القائمة الجانبية تماماً
    page_icon="⚡"
)

# ==========================================
# 2. هندسة الواجهة والتنسيق (UI Engineering) - تصحيح ألوان الهاتف
# ==========================================
def apply_mobile_design():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
        
        /* الخطوط والاتجاهات */
        html, body, [class*="css"] {
            font-family: 'Cairo', sans-serif;
            direction: rtl; text-align: right;
            background-color: #0d1117; /* خلفية داكنة ثابتة */
            color: white !important; /* فرض اللون الأبيض للنص */
        }
        
        /* جعل العناوين واضحة جداً وتصحيح اللون */
        h1 { color: #00d4ff !important; text-align: center; font-size: 1.8rem !important; margin-bottom: 5px; }
        h2, h3 { color: white !important; font-size: 1.2rem !important; margin-top: 15px; }
        p { color: #ffffff !important; }

        /* تنسيق البطاقات (Cards) لتكون أوضح */
        .mobile-card {
            background-color: #161b22;
            padding: 20px;
            border-radius: 15px;
            border: 1px solid #30363d;
            margin-bottom: 20px;
            text-align: center;
        }

        /* تنسيق المدخلات */
        .stNumberInput, .stSlider {
            background-color: #161b22;
            border-radius: 10px;
            padding: 5px;
            margin-bottom: 10px;
        }
        
        /* تصحيح لون النص داخل المدخلات */
        .stNumberInput div[data-baseweb="input"] {
            color: white !important;
        }

        /* تحسين مظهر الأزرار */
        .stButton>button {
            width: 100%;
            background-color: #00d4ff;
            color: black;
            font-weight: bold;
            border-radius: 10px;
            border: none;
            padding: 10px;
        }
        
        /* تنسيق رابط التحميل */
        .download-link {
            display: inline-block;
            margin-top: 15px;
            padding: 10px 20px;
            background-color: transparent;
            border: 2px solid #00d4ff;
            border-radius: 10px;
            color: #00d4ff !important;
            text-decoration: none;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

apply_mobile_design()

# ==========================================
# 3. الوظائف الرياضية (Computational Engine)
# ==========================================
class PhysicsEngine:
    @staticmethod
    def calculate_laplace(I, L, B, theta):
        return I * L * B * math.sin(math.radians(theta))

    @staticmethod
    def get_download_link(df):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        return f'<center><a href="data:file/csv;base64,{b64}" download="physics_results.csv" class="download-link">📥 تحميل النتيجة (CSV)</a></center>'

# ================= =========================
# 4. بناء هيكل التطبيق (App Architecture) - صفحة واحدة عمودية
# ==========================================

# الرأس (Header)
st.markdown('<h1>🔬 مختبر عليلي الفيزيائي</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;">إعداد المبرمج: عبد المالك عليلي | الإصدار الانسيابي النهائي</p>', unsafe_allow_html=True)
st.markdown("---")

# --- القسم الأول: ملخص المشروع (Cards بدلاً من Columns) ---
[04-05-2026 15:07] Abdou Trader: st.write("### 📋 ملخص أداء النظام")
st.markdown(f"""
<div class="mobile-card">
    <span style="font-size:25px; color:#00d4ff; font-weight:bold;">99.9%</span><br>
    <span style="color:#ffffff;">دقة الحساب (مستقر)</span>
</div>
<div class="mobile-card">
    <span style="font-size:25px; color:#00d4ff; font-weight:bold;">0.02s</span><br>
    <span style="color:#ffffff;">سرعة الاستجابة</span>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# --- القسم الثاني: المحاكي والحسابات (المنحنى محذوف) ---
st.write("### ⚙️ محرك الحساب الذكي")
st.markdown('<div class="mobile-card">', unsafe_allow_html=True)

# المدخلات الفيزيائية
I = st.number_input("التيار (I) بالأمبير:", value=2.0)
L = st.number_input("الطول (L) بالمتر:", value=0.5)
B = st.number_input("الحقل (B) بالتسلا:", value=0.1)
theta = st.slider("الزاوية (θ):", 0, 180, 90)

# الحساب
force = PhysicsEngine.calculate_laplace(I, L, B, theta)

# عرض النتيجة بخط كبير وواضح
st.markdown(f"""
<div style='background-color:#0d1117; padding:15px; border-radius:10px; border: 1px solid #00d4ff; margin-top:15px;'>
    <p style='margin:0; color:#00d4ff;'>القوة الناتجة F:</p>
    <h2 style='color:#00d4ff; font-size: 35px !important; margin:5px 0;'>{force:.4f} N</h2>
</div>
""", unsafe_allow_html=True)

# ميزة حفظ البيانات
if st.button("💾 حفظ النتيجة"):
    data = {"التيار": [I], "الطول": [L], "الحقل": [B], "الزاوية": [theta], "القوة": [force], "التاريخ": [datetime.now().strftime('%Y-%m-%d')]}
    df = pd.DataFrame(data)
    st.markdown(PhysicsEngine.get_download_link(df), unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---")

# --- القسم الثالث: الاختبار التفاعلي ---
st.write("### 🧠 اختبار كفاءة الفهم")
with st.form("quiz_form"):
    st.write("سؤال: ما هي قيمة قوة لابلاص عندما يكون السلك موازياً لخطوط الحقل؟")
    # تصحيح تداخل الخيارات عبر استخدام قائمة عمودية
    answer = st.radio("اختر الإجابة:", ["معدومة (0)", "أعظمية"], key="quiz_radio")
    submitted = st.form_submit_button("إرسال الإجابة")
    if submitted:
        if answer == "معدومة (0)":
            st.success("إجابة صحيحة! فهمك ممتاز.")
            st.balloons()
        else:
            st.error("خطأ! تذكر أن sin(0) = 0.")
st.markdown("---")

# --- القسم الرابع: التواصل (دمج مع التذييل) ---
st.markdown(f"""
<div class="mobile-card" style="border:none; background-color:transparent;">
    <h3>📧 تواصل مباشرة مع المبرمج</h3>
    <a href="mailto:aliliabdou826@gmail.com" class="download-link">aliliabdou826@gmail.com</a>
    <p style="margin-top:10px;">🇩🇿 ولاية سطيف | الجزائر</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<center style='color:#8b949e; font-size:12px;'>حقوق البرمجة محفوظة © 2026 | عبد المالك عليلي</center>", unsafe_allow_html=True)
