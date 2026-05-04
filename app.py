import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="موسوعة لابلاص الفيزيائية", page_icon="🔬", layout="centered")

# 2. هندسة المظهر الفاتح والألوان المنعشة (Light Mode)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    /* تنسيق الخلفية والنصوص */
    .stApp {
        background-color: #f0f2f6; /* لون فاتح مريح */
        font-family: 'Cairo', sans-serif;
        direction: rtl;
    }
    
    /* تصميم البطاقات الملونة */
    .physics-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 20px;
        border-left: 10px solid #ff4b4b;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        color: #31333f;
    }
    
    h1 { color: #ff4b4b !important; text-align: center; font-weight: 900; }
    h2 { color: #1f77b4 !important; }
    
    /* تأثيرات كرتونية */
    .emoji-art { font-size: 50px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. الواجهة الرسومية (أينشتاين والذرة)
st.markdown("<h1>⚛️ موسوعة القوى الفيزيائية</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # رسومات فيزيائية كرتونية
    st.markdown("""
    <div style="text-align:center;">
        <span style="font-size:70px;">👨‍🔬</span><br>
        <p style="color:#31333f; font-weight:bold;">"الخيال أهم من المعرفة" - ألبرت أينشتاين</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# 4. قسم قوة لابلاص (شرح فخيم بدون حسابات)
st.markdown("""
<div class="physics-card">
    <h2>🎯 ما هي قوة لابلاص؟</h2>
    <p>هي تلك القوة السحرية التي تنشأ عندما يمر تيار كهربائي داخل حقل مغناطيسي. تخيل السلك كأنه يقفز هارباً من المغناطيس!</p>
    <div style="text-align:center; font-size:40px;">🧲 ⚡ ➡️ 🏃</div>
</div>
""", unsafe_allow_html=True)

# 5. معلومات الذرة الكرتونية
st.markdown("""
<div class="physics-card" style="border-left-color: #1f77b4;">
    <h2>⚛️ في قلب المادة</h2>
    <p>تتكون الذرة من بروتونات ونيوترونات يحيط بها إلكترونات سريعة جداً. هذه الإلكترونات هي المسؤولة عن التيار الذي يولد لنا قوة لابلاص!</p>
    <div class="emoji-art">🌀✨</div>
</div>
""", unsafe_allow_html=True)

# 6. التوقيع المسيلي الفخور
st.markdown("---")
st.markdown(f"""
<div style="text-align:center; background-color:#ff4b4b; color:white; padding:15px; border-radius:15px;">
    <h3 style="color:white !important; margin:0;">إعداد المبرمج المبدع: عبد المالك عليلي</h3>
    <p style="margin:5px 0;">📍 ولاية المسيلة الأبية | الجزائر 🇩🇿</p>
    <p>📧 aliliabdou826@gmail.com</p>
</div>
""", unsafe_allow_html=True)

st.balloons()
[04-05-2026 15:23] Abdou Trader: import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="مختبر المسيلة للفيزياء", page_icon="🔬", layout="centered")

# 2. تصميم الواجهة الفاتحة (Light Mode)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    .stApp {
        background-color: #f8f9fa;
        font-family: 'Cairo', sans-serif;
        direction: rtl;
    }
    
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-right: 8px solid #4CAF50;
    }
    
    h1 { color: #2E7D32 !important; text-align: center; font-weight: 900; }
    h2 { color: #1565C0 !important; border-bottom: 2px solid #e0e0e0; padding-bottom: 10px; }
    .highlight { color: #d32f2f; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. العنوان والرسومات الكرتونية
st.markdown("<h1>🔬 مختبر قوة لابلاص المطور</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style="text-align:center;">
        <span style="font-size:80px;">👨‍🔬</span>
        <p style="color:#555;">بإشراف المبرمج: <b>عبد المالك عليلي</b></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# 4. استنتاج جهة القوة (قاعدة اليد اليمنى)
st.markdown("""
<div class="card">
    <h2>👋 كيف نحدد جهة القوة؟ (قاعدة اليد اليمنى)</h2>
    <p>لتحديد جهة القوة الكهرومغناطيسية، نستخدم أصابع اليد اليمنى كالتالي:</p>
    <ul style="list-style-type: none; padding: 0;">
        <li>🔹 <b>الإبهام:</b> يشير إلى جهة <span class="highlight">التيار الكهربائي (I)</span>.</li>
        <li>🔹 <b>السبابة:</b> تشير إلى جهة <span class="highlight">الحقل المغناطيسي (B)</span>.</li>
        <li>🔹 <b>الوسطى:</b> تشير إلى جهة <span class="highlight">قوة لابلاص (F)</span>.</li>
    </ul>
    <div style="text-align:center; font-size:40px; margin-top:10px;">🖐️ 📐 ✨</div>
</div>
""", unsafe_allow_html=True)



# 5. قسم الذرة وأينشتاين
st.markdown("""
<div class="card" style="border-right-color: #FF9800;">
    <h2>⚛️ العالم المجهري</h2>
    <p>أثبت أينشتاين أن كل شيء في الكون طاقة. وفي تجربتنا، تتحول الطاقة الكهربائية والمغناطيسية إلى <b>حركة فعلية</b> نراها بالعين المجردة!</p>
    <div style="text-align:center; font-size:50px;">🧪 ✨ 🏃</div>
</div>
""", unsafe_allow_html=True)

# 6. التوقيع النهائي (ولاية المسيلة)
st.markdown(f"""
<div style="text-align:center; background: linear-gradient(to left, #2E7D32, #4CAF50); color:white; padding:20px; border-radius:20px; margin-top:30px;">
    <h3 style="color:white !important; margin:0;">تم التطوير بكل فخر في ولاية المسيلة 🇩🇿</h3>
    <p style="margin:10px 0; font-size:18px;">المبرمج المبدع: <b>عبد المالك عليلي</b></p>
    <p style="font-size:14px;">2026 | مختبر الفيزياء الرقمي</p>
</div>
""", unsafe_allow_html=True)

st.balloons()
