import streamlit as st
import random

st.set_page_config(page_title="Python Quiz", page_icon="🧠")

# ---------------- Session State ----------------
if "start_quiz" not in st.session_state:
    st.session_state.start_quiz = False

if "player_name" not in st.session_state:
    st.session_state.player_name = ""

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False

# ---------------- Questions ----------------
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
    }, 
    {
        "Question" : "Which keyword is used to import a module?",
        "Options" : [
            "A. include",
            "B. import ",
            "C. using",
            "D. require"
        ],
        "Answer" : "B"
    },
    {
       "Question" : " Which method is called when an object is created?",
        "Options" : [
            "A. init()",
            "B. create()",
            "C. init()",
            "D. constructor()"
        ],
        "Answer": "C"
    },
    {
      "Question" : "Which keyword skips the current iteration? ",
      "Options" : [
           "A. break ",
           "B. continue",
           "C. pass",
           "D. skip"
      ],
      "Answer" : "B"
    },
    {
      "Question" : "Which keyword is used to stop a loop?",
      "Options" : [
          "A. break",
          "B. stop",
          "C. exit",
          "D. continue"
      ],
      "Answer" : "A"
    },
    {
        "Question" : "Which keyword handles an exception?",
        "Options" : [
            "A. catch", 
            "B. except",
            "C. error",
            "D. finally"
        ],
        "Answer" : "B"
    },
    {
        "Question" : "Which data type is mutable?",
        "Options" : [ 
            "A. tuple",
            "B. list",
            "C. string",  
            "D. frozenset"
           ],
           "Answer" : "B"
    }
]

# Shuffle questions once
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = questions.copy()
    random.shuffle(st.session_state.shuffled_questions)

# ---------------- Start Screen ----------------
if not st.session_state.start_quiz:
    st.title("🧠 Python Quiz Application")
    st.write("### Welcome to the Python Quiz! 🎉")

    name = st.text_input("👤 Enter Your Name")

    if st.button("🚀 Start Quiz"):
        if name.strip():
            st.session_state.player_name = name
            st.session_state.start_quiz = True
            st.rerun()
        else:
            st.warning("Please enter your name.")

    st.stop()

# ---------------- Result Screen ----------------
if st.session_state.quiz_finished:
    st.title("🎉 Quiz Completed")

    score = st.session_state.score
    total = len(questions)
    percentage = (score / total) * 100

    st.success(f"Congratulations, {st.session_state.player_name}!")
    st.write(f"## Score: {score}/{total}")
    st.write(f"## Percentage: {percentage:.2f}%")

    if percentage == 100:
        st.balloons()
        st.success("🏆 Perfect Score!")
    elif percentage >= 75:
        st.success("🎉 Excellent!")
    elif percentage >= 50:
        st.info("👍 Good Job!")
    else:
        st.warning("📚 Keep Practicing!")

    if st.button("🔄 Play Again"):
        st.session_state.start_quiz = False
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.quiz_finished = False

        st.session_state.shuffled_questions = questions.copy()
        random.shuffle(st.session_state.shuffled_questions)

        st.rerun()

    st.stop()

# ---------------- Quiz Screen ----------------
st.title("🧠 Python Quiz")

st.success(f"👋 Welcome, {st.session_state.player_name}")

index = st.session_state.current_question

st.progress((index + 1) / len(questions))

st.write(f"### Question {index + 1} of {len(questions)}")

question = st.session_state.shuffled_questions[index]

st.subheader(question["Question"])

answer = st.radio(
    "Choose your answer:",
    question["Options"],
    key=index
)

if st.button("Next ➡️"):

    if answer.startswith(question["Answer"]):
        st.session_state.score += 1

    if index == len(questions) - 1:
        st.session_state.quiz_finished = True
    else:
        st.session_state.current_question += 1

    st.rerun()
