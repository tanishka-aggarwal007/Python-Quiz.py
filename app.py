import streamlit as st

st.set_page_config(page_title="Python Quiz", page_icon="🧠")

st.title("🧠 Python Quiz Application")

questions = [
    {
        "Question": "Who developed Python?",
        "Options": [
            "A. James Gosling",
            "B. Guido van Rossum",
            "C. Dennis Ritchie",
            "D. Bjarne Stroustrup"
        ],
        "Answer": "B"
    },
    {
        "Question": "Which keyword is used to create a function in Python?",
        "Options": [
            "A. function",
            "B. define",
            "C. def",
            "D. func"
        ],
        "Answer": "C"
    },
    {
        "Question": "Which data type stores True/False values in Python?",
        "Options": [
            "A. int",
            "B. string",
            "C. float",
            "D. bool"
        ],
        "Answer": "D"
    },
    {
        "Question": "Which function is used to display output in Python?",
        "Options": [
            "A. input()",
            "B. output()",
            "C. print()",
            "D. display()"
        ],
        "Answer": "C"
    }
]

score = 0

for i, question in enumerate(questions):
    st.subheader(f"Question {i+1}")
    st.write(question["Question"])

    answer = st.radio(
        "Choose your answer:",
        question["Options"],
        key=i
    )

    if answer.startswith(question["Answer"]):
        score += 1

if st.button("Submit Quiz"):

    st.success(f"Your Score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100

    st.write(f"Percentage: {percentage:.2f}%")

    if percentage >= 75:
        st.balloons()
        st.success("🎉 Excellent!")
    elif percentage >= 50:
        st.info("👍 Good Job!")
    else:
        st.warning("📚 Keep Practicing!")