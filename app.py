import streamlit as st
if "start_quiz" not in st.session_state:
    st.session_state.start_quiz = False


st.set_page_config(page_title="Python Quiz", page_icon="🧠")

st.title("🧠 Python Quiz Application")
if not st.session_state.start_quiz:

    st.title("🧠 Python Quiz Application")

    st.write("### Welcome to the Python Quiz! 🎉")

    player_name = st.text_input("👤 Enter your Name")

    if st.button("🚀 Start Quiz"):

        if player_name.strip():

            st.session_state.player_name = player_name
            st.session_state.start_quiz = True
            st.rerun()

        else:
            st.warning("⚠️ Please enter your name first.")

    st.stop()


st.success(f"👋 Welcome, {st.session_state.player_name}!")
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

st.session_state.player_name

st.success(f"🎉 Congratulations, {st.session_state.player_name}!")

st.write(f"Your Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100

st.write(f"Percentage: {percentage:.2f}%")

if percentage >= 75:
        st.balloons()
        st.success("🎉 Excellent!")
elif percentage >= 50:
        st.info("👍 Good Job!")
else:
        st.warning("📚 Keep Practicing!")
