Questions = [
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
        "Question": "Which data type stores True/False values in Python ?",
        "Options" : [
            "A. int",
            "B. string",
            "C. Float",
            "D. bool"
        ],
        "Answer" : "D"
     },

     {
     "Question" : "Which function is used to display output in Python?",
     "Options" : ["A. input()",
                  "B. output()",
                  "C. print()",
                  "D. display()",
                  ],
                  "Answer" : "C"
     }
]
 
score = 0

for question in Questions:

    print(question["Question"])

    for option in question["Options"]:
        print(option)

    user_answer = input("Enter your answer: ").strip().upper()

    if user_answer == question["Answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong!")
        print("Correct Answer:", question["Answer"])
        print()

print("===== Quiz Finished =====")
print("Your Score:", score)
print("Total Questions:", len(Questions))

percentage = (score / len(Questions)) * 100
print("Percentage:", percentage, "%")

if percentage >= 75:
    print("🎉 Excellent!")
elif percentage >= 50:
    print("👍 Good Job!")
else:
    print("📚 Keep Practicing!")