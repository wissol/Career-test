import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="Career Test / اختبار تحديد المهنة", page_icon="🎯", layout="centered")

# صفحة اختيار اللغة وترحيب باسم مختلف
if 'lang' not in st.session_state:
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

# إذا اللغة عربية، نعرض الأسئلة بالعربية مع الترحيب باسم وصال
if 'lang' in st.session_state and st.session_state.lang == 'ar':
st.header("🎯 اختبار تحديد المهنة بأسئلة عميقة")
st.write("أنا وصال، أرحب بك وأدعوك للإجابة عن الأسئلة التالية بصدق لكي نساعدك في معرفة مهنتك المناسبة.")

questions = [
"إذا كان العالم بلا قيود مالية أو زمنية، ما المشروع الذي ستكرس له حياتك؟",
"أمامك قرار مصيري في حياتك، هل تفضل جمع كل المعلومات قبل الحسم أم الاعتماد على إحساسك؟ ولماذا؟",
"تخيل أنك مسؤول عن حل مشكلة عالمية (الفقر، تغير المناخ، التعليم...)، ما المشكلة التي تختارها وكيف تبدأ؟",
"إذا كان لديك فرصة لتعلّم مهارة جديدة خلال 24 ساعة، ما هي ولماذا اخترتها؟",
"متى شعرت آخر مرة أنك متحمس لدرجة أنك لم تستطع التوقف عن العمل أو التعلم؟ ماذا كنت تفعل؟",
"أيهما يلهمك أكثر: النجاح الشخصي الكبير أم رؤية تأثيرك على الآخرين؟",
"إذا تم حذف كل مؤهلاتك ودراستك السابقة، كيف ستقنع شركة أو شخصًا أن يثق بك؟",
"لو طلب منك شخص أن تشرح له 'من أنت' لكن بدون ذكر أي مهنة أو دراسة، كيف ستصف نفسك؟",
"إذا وضعتك في فريق من أشخاص أذكياء لكن شخصياتهم قوية ومختلفة، كيف ستجعلهم يعملون بانسجام؟",
"لو كان لديك كتاب واحد فقط لتقرأه كل سنة لبقية حياتك، أي كتاب سيكون ولماذا؟",
"إذا كان لديك ساعة إضافية كل يوم، كيف ستستغلها؟",
"أي موقف يجعلك تشعر أن الوقت يمر بسرعة شديدة؟",
"إذا أزلنا الخوف من الفشل من حياتك، ماذا ستجرب فورًا؟",
"اختر لونًا واحدًا وفسر لماذا يعبر عنك.",
"ما الشيء الذي لا يمكن أن تتخلى عنه في عملك مهما حدث؟",
"إذا قابلت نسخة منك في عالم موازٍ، ما النصيحة التي ستعطيها لك؟"
]

with st.form("career_form_ar"):
answers = []
for q in questions:
answer = st.text_area(q, "")
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

if scores[best_match] == 0:
st.warning("لم نجد كلمات كافية لتحديد مجال محدد بدقة، حاول أن تكون إجاباتك أكثر تفصيلًا.")
else:
if best_match == "الطب والتمريض":
st.success("🩺 يبدو أنك مناسب لمهن الطب مثل: الطبيب، الجراح، الممرض، المعالج الفيزيائي.")
elif best_match == "المجالات الإبداعية":
st.success("🎨 تميل للمهن الإبداعية مثل: مصمم جرافيك، مخرج، كاتب، فنان تشكيلي.")
elif best_match == "المجالات التحليلية":
st.success("📊 تميل للمهن التحليلية مثل: مهندس، عالم بيانات، محلل نظم، باحث علمي.")
elif best_match == "المجالات الاجتماعية":
st.success("💬 تميل للمهن الاجتماعية مثل: معلم، مدرب، أخصائي اجتماعي، قائد مشاريع مجتمعية.")
# إذا اللغة إنجليزية مع الترحيب باسم Wissol
if 'lang' in st.session_state and st.session_state.lang == 'en':
st.header("🎯 Deep Career Test")
st.write("I'm Wissol, welcome! Please answer the following questions honestly to help you discover your best career path.")

questions_en = [
"If the world had no financial or time constraints, what project would you dedicate your life to?",
"You have a critical decision to make. Do you prefer gathering all information before deciding or relying on your intuition? Why?",
"Imagine you are responsible for solving a global problem (poverty, climate change, education...), which problem would you choose and how would you start?",
"If you had the chance to learn a new skill within 24 hours, what would it be and why?",
"When was the last time you felt so excited that you couldn’t stop working or learning? What were you doing?",
"What inspires you more: great personal success or seeing the impact you have on others?",
"If all your qualifications and previous studies were erased, how would you convince a company or person to trust you?",
"If someone asked you to explain 'who you are' without mentioning any profession or study, how would you describe yourself?",
"If you were placed in a team of smart people with strong and different personalities, how would you make them work harmoniously?",
"If you had only one book to read every year for the rest of your life, which book would it be and why?",
"If you had an extra hour every day, how would you spend it?",
"What situation makes you feel that time passes very quickly?",
"If we removed the fear of failure from your life, what would you try immediately?",
"Choose one color and explain why it represents you.",
"What is something you can never give up in your work no matter what?",
"If you met a version of yourself in a parallel world, what advice would you give yourself?"
]

with st.form("career_form_en"):
answers_en = []
for q in questions_en:
answer = st.text_area(q, "")
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

if scores_en[best_match_en] == 0:
st.warning("Not enough keywords found to determine a specific field accurately, please provide more detailed answers.")
else:
if best_match_en == "Medical and Nursing":
st.success("🩺 You seem suitable for medical careers like: doctor, surgeon, nurse, physical therapist.")
elif best_match_en == "Creative Fields":
st.success("🎨 You tend to creative careers like: graphic designer, director, writer, visual artist.")
elif best_match_en == "Analytical Fields":
st.success("📊 You lean toward analytical careers like: engineer, data scientist, system analyst, researcher.")
elif best_match_en == "Social Fields":
st.success("💬 You lean toward social careers like: teacher, coach, social worker, community project leader.")

