# INVESTMENT QUIZ
# VERSION 1

# Import tkinter so we can create a GUI
import tkinter as tk

# Import messagebox so we can show warning messages
from tkinter import messagebox


# QUESTIONS

# This list stores all of the questions in the quiz.
# Each question is stored as a dictionary.
#
# "question" stores the question itself.
# "options" stores the possible answers.
# "scores" stores the score for each answer.
#
# For example:
# Option 1 = 1 point
# Option 2 = 2 points
# Option 3 = 3 points

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


# variables

# This variable stores the user's total score.
# It starts at 0 because the user has not answered
# any questions yet.
score = 0


# This keeps track of which question the user is on.
# Python starts counting from 0.
current_question = 0


# CREATE THE MAIN WINDOW

# Create the main Tkinter window.
root = tk.Tk()


# Set the title displayed at the top of the window.
root.title("Investment Recommendation Quiz")


# Set the size of the window.
# 600 = width
# 400 = height
root.geometry("600x400")


# TITLE

# Create a label for the title.
title = tk.Label(
    root,
    text="Investment Recommendation Quiz",
    font=("Arial", 20)
)


# Put the title inside the window.
title.pack(pady=20)


# QUESTION LABEL

# This label will display the current question.
question_label = tk.Label(
    root,
    text="",
    font=("Arial", 15),
    wraplength=500
)


# Put the question label into the window.
question_label.pack(pady=20)


# ANSWER VARIABLE

# IntVar is used by Tkinter to store which
# radio button the user has selected.
#
# -1 means that no answer has been selected yet.
choice = tk.IntVar(value=-1)


# RADIO BUTTONS

# This list will store all of the radio buttons.
buttons = []


# Create three radio buttons because each question
# has three possible answers.
for i in range(3):

    # Create a radio button.
    button = tk.Radiobutton(
        root,

        # The text will be changed when a question loads.
        text="",

        # Connect the button to the choice variable.
        variable=choice,

        # Each button gets a different value.
        value=i,

        font=("Arial", 12)
    )


    # Place the button on the screen.
    button.pack(
        anchor="w",
        padx=150
    )


    # Add the button to our list.
    buttons.append(button)


# LOAD QUESTION FUNCTION

# This function displays the current question.
def load_question():

    # Reset the selected answer.
    # This means the user must select an answer
    # for the new question.
    choice.set(-1)


    # Get the current question from the questions list.
    question = questions[current_question]


    # Change the question label to display
    # the current question.
    question_label.config(
        text=question["question"]
    )


    # Change each radio button to display
    # the current question's options.
    for i in range(3):

        buttons[i].config(
            text=question["options"][i]
        )


# NEXT QUESTION FUNCTION

# This function runs when the user presses Next.
def next_question():

    # We use global because we are changing
    # these variables inside the function.
    global score
    global current_question


    # Check if the user selected an answer.
    # -1 means no answer was selected.
    if choice.get() == -1:

        # Display a warning if they haven't
        # selected an answer.
        messagebox.showwarning(
            "No Answer",
            "Please select an answer."
        )

        # Stop the function here.
        return


    # Add the score from the selected answer
    # to the user's total score.
    #
    # choice.get() gives us the selected option.
    # The scores list tells us how many points
    # that option is worth.
    score += questions[current_question]["scores"][choice.get()]


    # Move to the next question.
    current_question += 1


    # Check whether there are still questions left.
    if current_question < len(questions):

        # If there are questions left,
        # display the next question.
        load_question()

    else:

        # If there are no questions left,
        # display the final result.
        show_results()

