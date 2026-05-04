import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import math
import base64
from datetime import datetime

# ==========================================
# 1. إعدادات النظام الأساسية (System Core)
# ==========================================
st.set_page_config(
    page_title="مختبر عليلي الفيزيائي | المبرمج المعتمد",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="⚡"
)

# ==========================================
# 2. هندسة الواجهة والتنسيق (UI Engineering)
# ==========================================
def apply_custom_design():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;900&display=swap');
        
        /* الخطوط والاتجاهات */
        html, body, [class*="css"] {
            font-family: 'Cairo', sans-serif;
            direction: rtl; text-align: right;
        }
        
        /* تصميم الحاويات الاحترافي */
        .main { background-color: #0d1117; }
        .stTabs [data-baseweb="tab-list"] { gap: 10px; }
        .stTabs [data-baseweb="tab"] {
            height: 50px; white-space: pre-wrap; background-color: #161b22;
            border-radius: 10px 10px 0 0; color: white; padding: 10px 20px;
        }
        .stTabs [aria-selected="true"] { background-color: #00d4ff !important; color: black !important; font-weight: bold; }
        
        /* تجميل المدخلات */
        .stNumberInput, .stSlider {
            border: 1px solid #30363d; border-radius: 12px; padding: 5px; background: #0d1117;
        }
        
        /* قسم النتائج */
        .result-card {
            background: linear-gradient(135deg, #1e2227 0%, #0d1117 100%);
            padding: 25px; border-radius: 20px; border: 2px solid #00d4ff;
            box-shadow: 0 10px 20px rgba(0,0,0,0.4); text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

apply_custom_design()

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
        return f'<a href="data:file/csv;base64,{b64}" download="physics_results.csv" style="color:#00d4ff; font-weight:bold;">📥 تحميل النتائج كملف Excel/CSV</a>'

# ================= =========================
# 4. بناء هيكل التطبيق (App Architecture)
# ==========================================

# الرأس (Header)
st.markdown('<div style="text-align:center;">', unsafe_allow_html=True)
st.title("🚀 المختبر الفيزيائي الرقمي - الإصدار 11.0")
st.write(f"المبرمج: عبد المالك عليلي | التاريخ: {datetime.now().strftime('%Y-%m-%d')}")
st.markdown('</div>', unsafe_allow_html=True)

# القائمة العلوية الحديثة (Modern Top Navigation)
tab_home, tab_calc, tab_quiz, tab_contact = st.tabs([
    "🏠 لوحة التحكم", "📊 المحاكي والحسابات", "🧠 اختبار الكفاءة", "📩 الدعم الفني"
])

# --- القسم الأول: لوحة التحكم ---
with tab_home:
    st.subheader("📋 ملخص المشروع")
    c1, c2, c3 = st.columns(3)
    c1.metric("دقة الحساب", "99.9%", "مستقر")
    c2.metric("سرعة الاستجابة", "0.02s", "-0.01s")
    c3.metric("إصدار الكود", "V11.0.4", "Final")
    
    st.info("""
    ملاحظة للمستخدم: هذا المختبر يعتمد على خوارزميات Python المتقدمة لحساب القوى المغناطيسية. 
    يمكنك استخدام التبويبات أعلاه للتنقل بين أجزاء البرنامج.
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Lorentz_force_on_a_current_carrying_wire.svg/600px-Lorentz_force_on_a_current_carrying_wire.svg.png", caption="توضيح بصري لجهة قوة لابلاص وقاعدة اليد اليمنى")
[04-05-2026 14:55] Abdou Trader: # --- القسم الثاني: المحاكي والحسابات ---
with tab_calc:
    st.subheader("⚙️ محرك المحاكاة الفيزيائية")
    col_input, col_viz = st.columns([1, 1.5])
    
    with col_input:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        I = st.number_input("التيار (I) بالأمبير:", value=2.0, help="شدة التيار المار في الناقل")
        L = st.number_input("الطول (L) بالمتر:", value=0.5)
        B = st.number_input("الحقل (B) بالتسلا:", value=0.1)
        theta = st.slider("الزاوية (θ):", 0, 180, 90)
        
        force = PhysicsEngine.calculate_laplace(I, L, B, theta)
        
        st.markdown(f"<h2 style='color:#00d4ff;'>F = {force:.4f} N</h2>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # ميزة حفظ البيانات
        if st.button("💾 حفظ النتيجة في الجدول"):
            data = {"التيار": [I], "الطول": [L], "الحقل": [B], "الزاوية": [theta], "القوة": [force]}
            df = pd.DataFrame(data)
            st.markdown(PhysicsEngine.get_download_link(df), unsafe_allow_html=True)

    with col_viz:
        angles = np.linspace(0, 180, 100)
        forces = [PhysicsEngine.calculate_laplace(I, L, B, a) for a in angles]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=angles, y=forces, name='منحنى القوة', line=dict(color='#00d4ff', width=4)))
        fig.add_trace(go.Scatter(x=[theta], y=[force], mode='markers', marker=dict(size=15, color='red'), name='الوضعية الحالية'))
        
        fig.update_layout(
            template="plotly_dark", 
            title="تحليل ديناميكي للقوة والزاوية",
            xaxis_title="الزاوية (درجة)", yaxis_title="القوة (نيوتن)",
            margin=dict(l=0, r=0, t=40, b=0),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

# --- القسم الثالث: الاختبار ---
with tab_quiz:
    st.subheader("🧠 نظام تقييم مستوى الفهم")
    with st.form("quiz_form"):
        st.write("سؤال: ما هي قيمة القوة عندما يكون السلك موازياً لخطوط الحقل؟")
        answer = st.radio("اختر الإجابة:", ["معدومة (0)", "أعظمية", "غير ثابتة"])
        submitted = st.form_submit_button("إرسال الإجابة")
        if submitted:
            if answer == "معدومة (0)":
                st.success("إجابة صحيحة! فهمك للقانون ممتاز.")
                st.balloons()
            else:
                st.error("إجابة خاطئة. تذكر أن sin(0) = 0.")

# --- القسم الرابع: التواصل ---
with tab_contact:
    st.markdown(f"""
    <div class="result-card">
        <h3>📧 مركز التواصل المباشر</h3>
        <p>للملاحظات التقنية أو طلب نسخ خاصة:</p>
        <a href="mailto:aliliabdou826@gmail.com" class="email-link" style="font-size:25px;">aliliabdou826@gmail.com</a>
        <br><br>
        <p>المبرمج: <b>عبد المالك عليلي</b></p>
        <p>📍 ولاية سطيف | الجزائر</p>
    </div>
    """, unsafe_allow_html=True)

# التذييل (Footer)
st.markdown("---")
st.markdown("<center>حقوق الملكية الفكرية والبرمجية محفوظة © 2026 | عبد المالك عليلي</center>", unsafe_allow_html=True)
