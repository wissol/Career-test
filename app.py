import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="Career Test / اختبار تحديد المهنة", page_icon="🎯", layout="centered")

# استايلات CSS لتحسين الخطوط، الألوان والإطارات
st.markdown("""
<style>
.question-box {
border: 2px solid #4A90E2;
border-radius: 10px;
padding: 15px;
margin-bottom: 20px;
background-color: #E8F0FE;
font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
font-size: 18px;
color: #333333;
}
.header {
color: #1F4E79;
font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
font-weight: bold;
}
.result-box {
border: 3px solid #1F4E79;
border-radius: 15px;
padding: 20px;
background-color: #D6E4F0;
margin-top: 30px;
}
.career-image {
width: 150px;
border-radius: 10px;
margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)


# صفحة اختيار اللغة وترحيب
if "lang" not in st.session_state:
st.title("مرحباً! أنا وصال، أنشأت هذا الاختبار لتساعدك على تحديد مهنتك.")
st.write("Welcome! I’m Wissol, I created this test to help you discover your career path.")
st.write("Please choose your language / من فضلك اختر لغتك:")

col1, col2 = st.columns(2)
with col1:
if st.button("العربية"):
st.session_state.lang = 'ar'
with col2:
if st.button("English"):
st.session_state.lang = 'en'
# أسئلة بالعربية
if 'lang' in st.session_state and st.session_state.lang == 'ar':
st.header("🎯 اختبار تحديد المهنة بأسئلة عميقة", anchor="header")
st.write("أنا وصال، أرحب بك وأدعوك للإجابة عن الأسئلة التالية بصدق لكي نساعدك في معرفة مهنتك المناسبة.")

questions = [
"إذا كان العالم بلا قيود مالية أو زمنية، ما المشروع الذي ستكرس له حياتك؟",
"أمامك قرار مصيري في حياتك، هل تفضل جمع كل المعلومات قبل الحسم أم الاعتماد على إحساسك؟ ولماذا؟",
"تخيل أنك مسؤول عن حل مشكلة عالمية (الفقر، تغير المناخ، التعليم...)، ما المشكلة التي تختارها وكيف تبدأ؟",
"إذا كان لديك فرصة لتعلّم مهارة جديدة خلال 24 ساعة، ما هي ولماذا اخترتها؟",
"متى شعرت آخر مرة أنك متحمس لدرجة أنك لم تستطع التوقف عن العمل أو التعلم؟ ماذا كنت تفعل؟",
# أسئلة عميقة إضافية
"كيف تتعامل مع الضغوطات في العمل، وهل تؤثر على أدائك؟",
"ما القيم والمبادئ التي لا تتنازل عنها في حياتك المهنية؟",
"صف لحظة شعرت فيها أنك قدمت أفضل ما لديك ولماذا كانت مهمة لك؟",
"كيف تفضل العمل: بشكل مستقل أم ضمن فريق؟ ولماذا؟",
"ما هو أكبر تحدي واجهته وكيف تغلبت عليه؟"
]

with st.form("career_form_ar"):
answers = []
for q in questions:
st.markdown(f'<div class="question-box">{q}</div>', unsafe_allow_html=True)
answer = st.text_area("", "", key=q)

answers.append(answer)
submitted = st.form_submit_button("تحليل الإجابات")

if submitted:
combined_text = " ".join(answers).lower()

medical_keywords = ["مساعدة", "إنقاذ", "صحة", "مرضى", "ألم", "علاج", "طبيب", "تمريض", "شفاء", "دم", "عملية"]
creative_keywords = ["إبداع", "فن", "ابتكار", "تصميم", "رسم", "كتابة", "موسيقى", "لوحة"]
analytical_keywords = ["تحليل", "أرقام", "منطق", "إحصاء", "هندسة", "برمجة", "رياضيات", "بحث"]
social_keywords = ["مجتمع", "تعليم", "تأثير", "إلهام", "تطوير", "تعاون", "خطاب"]

scores = {
"الطب والتمريض": sum(word in combined_text for word in medical_keywords),
"المجالات الإبداعية": sum(word in combined_text for word in creative_keywords),
"المجالات التحليلية": sum(word in combined_text for word in analytical_keywords),
"المجالات الاجتماعية": sum(word in combined_text for word in social_keywords)
}

best_match = max(scores, key=scores.get)

st.markdown('<div class="result-box">', unsafe_allow_html=True)


if scores[best_match] == 0:
st.warning("لم نجد كلمات كافية لتحديد مجال محدد بدقة، حاول أن تكون إجاباتك أكثر تفصيلًا.")
else:
if best_match == "الطب والتمريض":
st.success("🩺 يبدو أنك مناسب لمهن الطب مثل: الطبيب، الجراح، الممرض، المعالج الفيزيائي.")
st.image("https://cdn-icons-png.flaticon.com/512/2965/2965567.png", caption="مهن الطب", use_column_width=False, width=150)

elif best_match == "المجالات الإبداعية":
st.success("🎨 تميل للمهن الإبداعية مثل: مصمم جرافيك، مخرج، كاتب، فنان تشكيلي.")
st.image("https://cdn-icons-png.flaticon.com/512/685/685655.png", caption="المجالات الإبداعية", use_column_width=False, width=150)

elif best_match == "المجالات التحليلية":
st.success("📊 تميل للمهن التحليلية مثل: مهندس، عالم بيانات، محلل نظم، باحث علمي.")
st.image("https://cdn-icons-png.flaticon.com/512/1046/1046857.png", caption="المجالات التحليلية", use_column_width=False, width=150)

elif best_match == "المجالات الاجتماعية":
st.success("💬 تميل للمهن الاجتماعية مثل: معلم، مدرب، أخصائي اجتماعي، قائد مشاريع مجتمعية.")
st.image("https://cdn-icons-png.flaticon.com/512/3064/3064197.png", caption="المجالات الاجتماعية", use_column_width=False, width=150)

st.markdown('</div>', unsafe_allow_html=True)

# أسئلة بالإنجليزية
if 'lang' in st.session_state and st.session_state.lang == 'en':
st.header("🎯 Deep Career Test", anchor="header")

st.write("I'm Wissol, welcome! Please answer the following questions honestly to help you discover your best career path.")

questions_en = [
"If the world had no financial or time constraints, what project would you dedicate your life to?",
"You have a critical decision to make. Do you prefer gathering all information before deciding or relying on your intuition? Why?",
"Imagine you are responsible for solving a global problem (poverty, climate change, education...), which problem would you choose and how would you start?",
"If you had the chance to learn a new skill within 24 hours, what would it be and why?",
"When was the last time you felt so excited that you couldn’t stop working or learning? What were you doing?",
# deep questions added
"How do you handle stress at work, and does it affect your performance?",
"What are the values and principles you never compromise on in your professional life?",
"Describe a moment when you gave your best and why it was important to you.",
"Do you prefer working independently or within a team? Why?",
"What is the biggest challenge you've faced and how did you overcome it?"

]

with st.form("career_form_en"):
answers_en = []
for q in questions_en:
st.markdown(f'<div class="question-box">{q}</div>', unsafe_allow_html=True)
answer = st.text_area("", "", key=q)

answers_en.append(answer)
submitted_en = st.form_submit_button("Analyze Answers")

if submitted_en:
combined_text_en = " ".join(answers_en).lower()

medical_keywords_en = ["help", "save", "health", "patients", "pain", "treatment", "doctor", "nurse", "heal", "blood", "surgery"]
creative_keywords_en = ["creativity", "art", "innovation", "design", "drawing", "writing", "music", "painting"]
analytical_keywords_en = ["analysis", "numbers", "logic", "statistics", "engineering", "programming", "math", "research"]
social_keywords_en = ["community", "education", "impact", "inspiration", "development", "collaboration", "speech"]

scores_en = {
"Medical and Nursing": sum(word in combined_text_en for word in medical_keywords_en),
"Creative Fields": sum(word in combined_text_en for word in creative_keywords_en),
"Analytical Fields": sum(word in combined_text_en for word in analytical_keywords_en),
"Social Fields": sum(word in combined_text_en for word in social_keywords_en)
}

best_match_en = max(scores_en, key=scores_en.get)

st.markdown('<div class="result-box">', unsafe_allow_html=True)


if scores_en[best_match_en] == 0:
st.warning("Not enough keywords found to determine a specific field accurately, please provide more detailed answers.")
else:
if best_match_en == "Medical and Nursing":
st.success("🩺 You seem suitable for medical careers like: doctor, surgeon, nurse, physical therapist.")
st.image("https://cdn-icons-png.flaticon.com/512/2965/2965567.png", caption="Medical Careers", use_column_width=False, width=150)

elif best_match_en == "Creative Fields":
st.success("🎨 You tend to creative careers like: graphic designer, director, writer, visual artist.")
st.image("https://cdn-icons-png.flaticon.com/512/685/685655.png", caption="Creative Fields", use_column_width=False, width=150)

elif best_match_en == "Analytical Fields":
st.success("📊 You lean toward analytical careers like: engineer, data scientist, system analyst, researcher.")
st.image("https://cdn-icons-png.flaticon.com/512/1046/1046857.png", caption="Analytical Fields", use_column_width=False, width=150)

elif best_match_en == "Social Fields":
st.success("💬 You lean toward social careers like: teacher, coach, social worker, community project leader.")
st.image("https://cdn-icons-png.flaticon.com/512/3064/3064197.png", caption="Social Fields", use_column_width=False, width=150)

st.markdown('</div>', unsafe_allow_html=True)
