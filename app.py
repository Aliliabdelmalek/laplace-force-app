[04-05-2026 14:31] Abdou Trader: import streamlit as st
import numpy as np
import plotly.graph_objects as go
import math
import random

# --- إعدادات الصفحة الفخمة ---
st.set_page_config(page_title="مختبر عليلي العالمي V8", layout="wide", page_icon="⚡")

# --- تنسيق CSS لإبهار الزملاء ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }
    .stApp { background: linear-gradient(to bottom, #000428, #004e92); color: white; }
    .quiz-box { background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 15px; border: 2px dashed #00d4ff; }
    .stButton>button { background: #00d4ff; color: #000; font-weight: bold; border-radius: 10px; transition: 0.3s; }
    .stButton>button:hover { transform: scale(1.05); background: #fff; }
    </style>
    """, unsafe_allow_html=True)

# --- العنوان الرئيسي بتأثير بصري ---
st.markdown('<h1 style="text-align:center; color:#00d4ff; font-size:50px;">🚀 مختبر عليلي للفيزياء النووية والمغناطيسية</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size:20px;">المبرمج المعتمد: عبد المالك عليلي | نسخة 2026 العالمية</p>', unsafe_allow_html=True)

# --- القائمة الجانبية المزدحمة بالأدوات ---
with st.sidebar:
    st.title("🛠️ الأدوات الذكية")
    page = st.selectbox("اختر القسم:", ["📊 الحاسبة والرسوم", "🌀 الحقول والتحويلات", "🧠 اختبر ذكاءك الفيزيائي"])
    st.write("---")
    st.markdown("### 🔌 محول الوحدات السريع")
    val = st.number_input("القيمة المراد تحويلها:", value=1.0)
    unit_from = st.selectbox("من:", ["cm", "mm", "mA", "mT"])
    if unit_from == "cm": res_unit = val / 100 ; target = "m"
    elif unit_from == "mm": res_unit = val / 1000 ; target = "m"
    elif unit_from == "mA": res_unit = val / 1000 ; target = "A"
    else: res_unit = val / 1000 ; target = "T"
    st.success(f"النتيجة: {res_unit} {target}")

# --- 1. قسم الحاسبة والرسوم ---
if page == "📊 الحاسبة والرسوم":
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("🧮 حساب قوة لابلاص")
        I = st.number_input("التيار (A):", value=2.0)
        B = st.number_input("الحقل (T):", value=0.5)
        L = st.number_input("الطول (m):", value=1.0)
        ang = st.slider("الزاوية θ:", 0, 180, 90)
        force = I * L * B * math.sin(math.radians(ang))
        st.metric("النتيجة النهائية", f"{force:.4f} N", delta="قوة لابلاص")
    
    with col2:
        angles = np.linspace(0, 180, 100)
        forces = I * L * B * np.sin(np.radians(angles))
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=angles, y=forces, line=dict(color='#00d4ff', width=4)))
        fig.update_layout(title="تحليل تغير القوة", template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

# --- 2. قسم الحقول والتحويلات ---
elif page == "🌀 الحقول والتحويلات":
    st.header("🌀 حاسبة الحقول المغناطيسية الشاملة")
    mode = st.tabs(["سلك مستقيم", "وشيعة مسطحة", "وشيعة حلزونية"])
    
    with mode[0]:
        st.write("### القانون: $B = 2 \cdot 10^{-7} \cdot I / d$")
        i_s = st.number_input("التيار:", value=1.0, key="is")
        d_s = st.number_input("المسافة (m):", value=0.1, key="ds")
        st.info(f"B = {(2e-7 * i_s / d_s):.2e} T")
    
    with mode[1]:
        st.write("### القانون: $B = \mu_0 \cdot N \cdot I / 2R$")
        n_m = st.number_input("عدد اللفات:", value=50, key="nm")
        i_m = st.number_input("التيار:", value=2.0, key="im")
        r_m = st.number_input("نصف القطر (m):", value=0.05, key="rm")
        res_m = (4*math.pi*1e-7 * n_m * i_m) / (2*r_m)
        st.info(f"B = {res_m:.2e} T")
        
    with mode[2]:
        st.write("### القانون: $B = \mu_0 \cdot n \cdot I$")
        n_l = st.number_input("عدد اللفات:", value=500, key="nl")
        l_l = st.number_input("الطول (m):", value=0.2, key="ll")
        i_l = st.number_input("التيار:", value=3.0, key="il")
        res_l = (4*math.pi*1e-7 * n_l * i_l) / l_l
        st.info(f"B = {res_l:.2e} T")
[04-05-2026 14:31] Abdou Trader: # --- 3. قسم الاختبار (The Quiz) ---
elif page == "🧠 اختبر ذكاءك الفيزيائي":
    st.header("📝 تحدي المبرمج عبد المالك")
    st.write("اجب على هذا السؤال لترى إذا كنت مبرمجاً ذكياً:")
    
    q = "متى تكون قوة لابلاص أعظمية؟"
    options = ["عندما تكون الزاوية 0", "عندما تكون الزاوية 90", "عندما يكون التيار معدوماً"]
    ans = st.radio("اختر الإجابة:", options)
    
    if st.button("تحقق من الإجابة"):
        if ans == "عندما تكون الزاوية 90":
            st.success("إجابة عبقرية! تستحق أن تكون مبرمجاً!")
            st.balloons()
        else:
            st.error("حاول مجدداً، الفيزياء تحتاج تركيزاً!")

st.markdown("---")
st.markdown("<center>صُنع بكل إبداع بواسطة <b>عبد المالك عليلي</b> | الجزائر 🇩🇿 2026</center>", unsafe_allow_html=True)
[04-05-2026 14:34] Abdou Trader: import streamlit as st
import numpy as np
import plotly.graph_objects as go
import math

# --- إعدادات الصفحة الاحترافية ---
st.set_page_config(page_title="مختبر عليلي الفيزيائي الشامل", layout="wide", page_icon="🧲")

# --- تنسيق CSS لإبهار المستخدمين ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }
    .stApp { background: linear-gradient(135deg, #0f2027, #203a43, #2c5364); color: white; }
    .main-header { background: rgba(255, 255, 255, 0.1); padding: 30px; border-radius: 20px; border: 1px solid #00d4ff; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
    .calc-card { background: rgba(0, 0, 0, 0.3); padding: 20px; border-radius: 15px; border-right: 5px solid #00d4ff; }
    .email-link { color: #00d4ff !important; font-weight: 900; text-decoration: none; font-size: 1.3rem; }
    .email-link:hover { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# --- القائمة الجانبية (Sidebar) ---
with st.sidebar:
    st.markdown("## ⚙️ مركز التحكم")
    page = st.radio("اختر القسم:", ["🏠 المختبر الرئيسي", "🌀 حاسبة الحقول (B)", "🧠 اختبار الذكاء", "📧 تواصل معي"])
    
    st.write("---")
    st.markdown("### 🔌 محول الوحدات الذكي")
    u_val = st.number_input("القيمة:", value=1.0)
    u_type = st.selectbox("من:", ["cm (سنتيمتر)", "mm (ميليمتر)", "mA (ميلي أمبير)", "mT (ميلي تسلا)"])
    
    # منطق التحويل
    converted = u_val / 100 if "cm" in u_type else u_val / 1000
    target_unit = "m" if "m" in u_type else ("A" if "A" in u_type else "T")
    st.code(f"{converted} {target_unit}")
    
    st.write("---")
    st.markdown(f"المبرمج: عبد المالك عليلي")
    st.markdown(f'<a href="mailto:aliliabdou826@gmail.com" class="email-link">📩 أرسل ملاحظة</a>', unsafe_allow_html=True)

# --- واجهة المختبر الرئيسي ---
if page == "🏠 المختبر الرئيسي":
    st.markdown('<div class="main-header"><h1>🔬 موسوعة المغناطيسية العالمية</h1><p>الإصدار النهائي المطور بواسطة عبد المالك عليلي</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown('<div class="calc-card"><h3>🎯 حاسبة قوة لابلاص</h3>', unsafe_allow_html=True)
        I = st.number_input("شدة التيار I (A):", value=2.0)
        L = st.number_input("طول الناقل L (m):", value=0.5)
        B = st.number_input("شدة الحقل B (T):", value=0.1)
        theta = st.slider("الزاوية (θ) بالدرجات:", 0, 180, 90)
        
        force = I * L * B * math.sin(math.radians(theta))
        st.metric("القوة الناتجة F", f"{force:.4f} Newton")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.subheader("📊 التحليل البياني للعلاقة")
        angles = np.linspace(0, 180, 100)
        forces = I * L * B * np.sin(np.radians(angles))
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=angles, y=forces, mode='lines', line=dict(color='#00d4ff', width=3)))
        # إضافة نقطة القيمة الحالية
        fig.add_trace(go.Scatter(x=[theta], y=[force], mode='markers', marker=dict(size=12, color='red'), name='القيمة الحالية'))
        fig.update_layout(template="plotly_dark", title="تغير القوة بتغير الزاوية", margin=dict(l=10, r=10, t=40, b=10))
        st.plotly_chart(fig, use_container_width=True)

# --- واجهة حاسبة الحقول ---
elif page == "🌀 حاسبة الحقول (B)":
    st.header("🌀 حساب شدة الحقل المغناطيسي للناقل")
    tab1, tab2, tab3 = st.tabs(["سلك مستقيم", "وشيعة مسطحة", "وشيعة طويلة"])
    
    with tab1:
        st.markdown('<div class="calc-card">', unsafe_allow_html=True)
        i1 = st.number_input("التيار I (A):", value=2.0, key="i1")
        d1 = st.number_input("المسافة d (m):", value=0.02)
        b1 = (2e-7 * i1) / d1
        st.info(f"النتيجة: B = {b1:.2e} Tesla")
        st.markdown('</div>', unsafe_allow_html=True)
[04-05-2026 14:34] Abdou Trader: with tab2:
        st.markdown('<div class="calc-card">', unsafe_allow_html=True)
        n2 = st.number_input("عدد اللفات N:", value=100)
        i2 = st.number_input("التيار I (A):", value=1.5, key="i2")
        r2 = st.number_input("نصف القطر R (m):", value=0.05)
        b2 = (2 * math.pi * 1e-7 * n2 * i2) / r2
        st.info(f"النتيجة: B = {b2:.2e} Tesla")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="calc-card">', unsafe_allow_html=True)
        n3 = st.number_input("عدد اللفات الكلي N:", value=500)
        l3 = st.number_input("طول الوشيعة L (m):", value=0.2)
        i3 = st.number_input("التيار I (A):", value=3.0, key="i3")
        b3 = (4 * math.pi * 1e-7 * n3 * i3) / l3
        st.info(f"النتيجة: B = {b3:.2e} Tesla")
        st.markdown('</div>', unsafe_allow_html=True)

# --- واجهة الاختبار ---
elif page == "🧠 اختبار الذكاء":
    st.header("🧠 تحدي العباقرة")
    st.write("سؤال من المبرمج عبد المالك:")
    q = st.radio("إذا كانت شدة الحقل موازية للناقل (θ = 0)، كم تكون قوة لابلاص؟", ["أعظمية", "معدومة", "متوسطة"])
    if st.button("تحقق"):
        if q == "معدومة":
            st.success("عبقري! إجابة صحيحة.")
            st.balloons()
        else:
            st.error("خطأ! راجع درس الزوايا في قسم الرسوم البيانية.")

# --- واجهة التواصل ---
elif page == "📧 تواصل معي":
    st.markdown("""
        <div class="main-header">
            <h2>اتصل بالمبرمج الرسمي</h2>
            <p>يسعدني تلقي آرائكم واقتراحاتكم لتطوير المشاريع القادمة</p>
            <br>
            <a href="mailto:aliliabdou826@gmail.com" class="email-link">aliliabdou826@gmail.com</a>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown(f"<center>صُنع بكل فخر بواسطة عبد المالك عليلي | 🇩🇿 الجزائر 2026</center>", unsafe_allow_html=True)
