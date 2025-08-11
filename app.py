person to trust you?",
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

