# ==========================================
# INVESTMENT RECOMMENDATION QUIZ
# VERSION 2
# ==========================================

# Import tkinter for the GUI.
import tkinter as tk

# Import messagebox for warning messages.
from tkinter import messagebox


# ==========================================
# QUESTIONS
# ==========================================

# Store all questions inside a list.
questions = [

    {
        "question": "How long do you want to invest for?",

        "options": [
            "Less than 1 year",
            "1-5 years",
            "More than 5 years"
        ],

        "scores": [1, 2, 3]
    },


    {
        "question": "If your investment lost 20%, what would you do?",

        "options": [
            "Sell it",
            "Wait",
            "Buy more"
        ],

        "scores": [1, 2, 3]
    },


    {
        "question": "How much risk are you comfortable with?",

        "options": [
            "Low",
            "Medium",
            "High"
        ],

        "scores": [1, 2, 3]
    },


    {
        "question": "What is your main investment goal?",

        "options": [
            "Keep my money safe",
            "Earn extra money",
            "Grow my wealth"
        ],

        "scores": [1, 2, 3]
    },


    {
        "question": "How much investing experience do you have?",

        "options": [
            "None",
            "Some",
            "A lot"
        ],

        "scores": [1, 2, 3]
    }
]


# ==========================================
# VARIABLES
# ==========================================

# Store the user's score.
score = 0


# Store the current question number.
current_question = 0


# This list stores the answers the user has selected.
# It allows the user to go back to previous questions.
answers = []


# ==========================================
# MAIN WINDOW
# ==========================================

root = tk.Tk()

root.title("Investment Recommendation Quiz")

root.geometry("650x500")


# ==========================================
# START QUIZ FUNCTION
# ==========================================

def start_quiz():

    # We need to change these variables,
    # so we use global.
    global score
    global current_question


    # Get the name typed into the Entry box.
    name = name_entry.get()


    # Check whether the user entered a name.
    if name == "":

        messagebox.showwarning(
            "Name Required",
            "Please enter your name."
        )

        return


    # Reset the score.
    score = 0


    # Reset the question number.
    current_question = 0


    # Delete any previous answers.
    answers.clear()


    # Hide the name screen.
    name_frame.pack_forget()


    # Show the quiz screen.
    quiz_frame.pack(
        fill="both",
        expand=True
    )


    # Display the first question.
    load_question()


# ==========================================
# LOAD QUESTION FUNCTION
# ==========================================

def load_question():

    # Clear the selected radio button.
    choice.set(-1)


    # Get the current question.
    question = questions[current_question]


    # Display the question.
    question_label.config(
        text=question["question"]
    )


    # Display the question number.
    progress_label.config(
        text=f"Question {current_question + 1} "
             f"of {len(questions)}"
    )


    # Change the text of the radio buttons.
    for i in range(3):

        buttons[i].config(
            text=question["options"][i]
        )


# ==========================================
# NEXT QUESTION
# ==========================================

def next_question():

    global score
    global current_question


    # Make sure an answer has been selected.
    if choice.get() == -1:

        messagebox.showwarning(
            "No Answer",
            "Please select an answer."
        )

        return


    # Check if the user is changing
    # an answer they previously selected.
    if current_question < len(answers):

        # Get their old answer.
        old_answer = answers[current_question]


        # Remove the old score.
        score -= questions[current_question]["scores"][old_answer]


        # Store their new answer.
        answers[current_question] = choice.get()


    else:

        # Store the answer if this is
        # the first time answering the question.
        answers.append(choice.get())


    # Add the new answer's score.
    score += questions[current_question]["scores"][choice.get()]


    # Move to the next question.
    current_question += 1


    # Check if there are more questions.
    if current_question < len(questions):

        load_question()

    else:

        show_results()


# ==========================================
# BACK BUTTON
# ==========================================

def previous_question():

    global current_question


    # Make sure we are not already
    # on the first question.
    if current_question > 0:

        # Move back one question.
        current_question -= 1


        # Show the user's previous answer.
        choice.set(
            answers[current_question]
        )


        # Load the previous question.
        load_question()


# ==========================================
# SHOW RESULTS
# ==========================================

def show_results():

    # Hide the quiz screen.
    quiz_frame.pack_forget()


    # Show the results screen.
    results_frame.pack(
        fill="both",
        expand=True
    )


    # Get the user's name.
    name = name_entry.get()


    # Decide the risk profile.
    if score <= 7:

        profile = "Conservative"

        recommendation = (
            "Savings accounts\n"
            "Term deposits\n"
            "Government bonds"
        )


        explanation = (
            "You prefer lower risk investments."
        )


    elif score <= 11:

        profile = "Moderate"

        recommendation = (
            "Index funds\n"
            "Balanced funds\n"
            "Bonds"
        )


        explanation = (
            "You are comfortable with some risk."
        )


    else:

        profile = "Growth"

        recommendation = (
            "Growth ETFs\n"
            "Shares\n"
            "Global index funds"
        )


        explanation = (
            "You are comfortable with higher risk."
        )


    # Display the results.
    result_label.config(
        text=(
            f"{name}, your risk profile is:\n\n"

            f"{profile}\n\n"

            f"Score: {score}/15\n\n"

            f"{explanation}\n\n"

            f"Suggested investments:\n"
            f"{recommendation}"
        )
    )


# ==========================================
# RESTART FUNCTION
# ==========================================

def restart():

    # Hide the results screen.
    results_frame.pack_forget()


    # Clear the name.
    name_entry.delete(
        0,
        tk.END
    )


    # Show the start screen.
    name_frame.pack(
        fill="both",
        expand=True
    )


# ==========================================
# NAME SCREEN
# ==========================================

# Create a frame to hold the starting screen.
name_frame = tk.Frame(root)


# Create the title.
title = tk.Label(
    name_frame,
    text="Investment Recommendation Quiz",
    font=("Arial", 22)
)

title.pack(pady=40)


# Ask for the user's name.
name_label = tk.Label(
    name_frame,
    text="Enter your name:",
    font=("Arial", 14)
)

name_label.pack()


# Create a text box where the user
# can type their name.
name_entry = tk.Entry(
    name_frame,
    font=("Arial", 14)
)

name_entry.pack(pady=10)


# Create the Start Quiz button.
start_button = tk.Button(
    name_frame,
    text="Start Quiz",
    command=start_quiz
)

start_button.pack(pady=20)


# Display the starting screen.
name_frame.pack(
    fill="both",
    expand=True
)


# ==========================================
# QUIZ SCREEN
# ==========================================

quiz_frame = tk.Frame(root)


# Show the question number.
progress_label = tk.Label(
    quiz_frame,
    text="",
    font=("Arial", 12)
)

progress_label.pack(pady=20)


# Display the question.
question_label = tk.Label(
    quiz_frame,
    text="",
    font=("Arial", 17),
    wraplength=550
)

question_label.pack(pady=20)


# Store the selected answer.
choice = tk.IntVar(value=-1)


# Store the radio buttons.
buttons = []


# Create three radio buttons.
for i in range(3):

    button = tk.Radiobutton(
        quiz_frame,
        text="",
        variable=choice,
        value=i,
        font=("Arial", 13)
    )

    button.pack(
        anchor="w",
        padx=180,
        pady=5
    )

    buttons.append(button)


# Create a frame for the navigation buttons.
button_frame = tk.Frame(quiz_frame)

button_frame.pack(pady=30)


# Create the Back button.
back_button = tk.Button(
    button_frame,
    text="Back",
    command=previous_question
)

back_button.grid(
    row=0,
    column=0,
    padx=10
)


# Create the Next button.
next_button = tk.Button(
    button_frame,
    text="Next",
    command=next_question
)

next_button.grid(
    row=0,
    column=1,
    padx=10
)


# ==========================================
# RESULTS SCREEN
# ==========================================

results_frame = tk.Frame(root)


# Results title.
result_title = tk.Label(
    results_frame,
    text="Your Results",
    font=("Arial", 22)
)

result_title.pack(pady=30)


# This label will display the result.
result_label = tk.Label(
    results_frame,
    text="",
    font=("Arial", 14),
    justify="center"
)

result_label.pack(pady=20)


# Create the Retake button.
restart_button = tk.Button(
    results_frame,
    text="Retake Quiz",
    command=restart
)

restart_button.pack(pady=20)


# Disclaimer.
disclaimer = tk.Label(
    results_frame,
    text="For educational purposes only. Not financial advice.",
    font=("Arial", 9)
)

disclaimer.pack()


# ==========================================
# RUN PROGRAM
# ==========================================

root.mainloop()