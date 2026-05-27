from tkinter import *

# ---------------- WINDOW ----------------
root = Tk()
root.title("Quiz App")
root.geometry("1000x1000")

# ---------------- DATA ----------------
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
        "answer": "Delhi"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is H2O commonly known as?",
        "options": ["Oxygen", "Hydrogen", "Water", "Salt"],
        "answer": "Water"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Helium"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": "Pacific"
    },
    {
        "question": "Who wrote 'Ramayana'?",
        "options": ["Valmiki", "Tulsidas", "Kalidasa", "Ved Vyasa"],
        "answer": "Valmiki"
    },
    {
        "question": "Which is the hardest natural substance?",
        "options": ["Gold", "Iron", "Diamond", "Silver"],
        "answer": "Diamond"
    },
    {
        "question": "What is the square root of 144?",
        "options": ["10", "11", "12", "13"],
        "answer": "12"
    },
    {
        "question": "Which organ pumps blood in the human body?",
        "options": ["Lungs", "Brain", "Heart", "Kidney"],
        "answer": "Heart"
    },
    {
        "question": "Which is the fastest land animal?",
        "options": ["Lion", "Cheetah", "Horse", "Tiger"],
        "answer": "Cheetah"
    },
    {
        "question": "Which is the national bird of India?",
        "options": ["Crow", "Peacock", "Sparrow", "Eagle"],
        "answer": "Peacock"
    },
    {
        "question": "What is the boiling point of water?",
        "options": ["90°C", "80°C", "100°C", "120°C"],
        "answer": "100°C"
    },
    {
        "question": "Which instrument is used to measure temperature?",
        "options": ["Barometer", "Thermometer", "Speedometer", "Hygrometer"],
        "answer": "Thermometer"
    },
    {
        "question": "Which is the largest planet in our solar system?",
        "options": ["Earth", "Saturn", "Jupiter", "Neptune"],
        "answer": "Jupiter"
    },
    {
        "question": "Which metal is liquid at room temperature?",
        "options": ["Iron", "Mercury", "Copper", "Aluminium"],
        "answer": "Mercury"
    },
    {
        "question": "What is the value of Pi (approx)?",
        "options": ["2.14", "3.14", "3.41", "4.13"],
        "answer": "3.14"
    },
    {
        "question": "Which is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": "2"
    },
    {
        "question": "Which part of the plant makes food?",
        "options": ["Root", "Stem", "Leaf", "Flower"],
        "answer": "Leaf"
    },
    {
        "question": "Which country is known as the Land of Rising Sun?",
        "options": ["China", "Japan", "Korea", "India"],
        "answer": "Japan"
    }
]

question_index = 0
score = 0

# ---------------- FUNCTIONS ----------------

def load_question():
    current_question = questions[question_index]

    question_label.config(text=current_question["question"])

    option1.config(text=current_question["options"][0])
    option2.config(text=current_question["options"][1])
    option3.config(text=current_question["options"][2])
    option4.config(text=current_question["options"][3])


def check_answer(selected_option):
    global question_index, score

    current_question = questions[question_index]

    if selected_option == current_question["answer"]:
        question_label.config(text="Correct ✅")
        score += 1


    else:
        question_label.config(text="INCORRECT")

    question_index += 1
    

    if question_index < len(questions):
        load_question()

    else:
        question_label.config(text=f"Quiz Finished!\nScore: {score}/{len(questions)}")

    print(selected_option)


# ---------------- UI ---------------- #

title_label = Label(
    root,
    text="QUIZ APP",
    font=("Algerian", 20)
)
title_label.pack(pady=10)

question_label = Label(
    root,
    text="Question comes here",
    font=("Comic Sans", 14),
    wraplength=400
)
question_label.pack(pady=20)

option1 = Button(root, text="Option 1",
                 width=20,
                 command=lambda: check_answer(option1.cget("text")))
option1.pack(pady=5)

option2 = Button(root, text="Option 2",
                 width=20,
                 command=lambda: check_answer(option2.cget("text")))
option2.pack(pady=5)

option3 = Button(root, text="Option 3",
                 width=20,
                 command=lambda: check_answer(option3.cget("text")))
option3.pack(pady=5)

option4 = Button(root, text="Option 4",
                 width=20,
                 command=lambda: check_answer(option4.cget("text")))
option4.pack(pady=5)

# ---------------- START ----------------

load_question()

root.mainloop()