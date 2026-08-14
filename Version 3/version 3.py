# ==========================================
# INVESTMENT RECOMMENDATION QUIZ
# VERSION 3
# ==========================================

# Import tkinter to create the GUI.
import tkinter as tk

# Import messagebox for warning messages.
from tkinter import messagebox

# Import csv so we can save quiz results.
import csv


# ==========================================
# QUESTIONS
# ==========================================

# Store the questions in a list.
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

# Total score.
score = 0


# Current question.
current_question = 0


# Store previous answers.
answers = []


# ==========================================
# MAIN WINDOW
# ==========================================

# Create the main window.
root = tk.Tk()


# Set the title.
root.title("Investment Recommendation Quiz")


# Set the window size.
root.geometry("700x550")


# ==========================================
# START QUIZ
# ==========================================

def start_quiz():

    global score
    global current_question


    # Get the user's name.
    name = name_entry.get()


    # Make sure a name was entered.
    if name == "":

        messagebox.showwarning(
            "Name Required",
            "Please enter your name."
        )

        return


    # Reset the score.
    score = 0


    # Start at the first question.
    current_question = 0


    # Remove any previous answers.
    answers.clear()


    # Hide the name screen.
    name_frame.pack_forget()


    # Show the quiz screen.
    quiz_frame.pack(
        fill="both",
        expand=True
    )


    # Load the first question.
    load_question()


# ==========================================
# LOAD QUESTION
# ==========================================

def load_question():

    # Clear the selected answer.
    choice.set(-1)


    # Get the current question.
    question = questions[current_question]


    # Display the question.
    question_label.config(
        text=question["question"]
    )


    # Display progress.
    progress_label.config(
        text=f"Question {current_question + 1} "
             f"of {len(questions)}"
    )


    # Update the answer buttons.
    for i in range(3):

        buttons[i].config(
            text=question["options"][i]
        )


    # Disable Back on the first question.
    if current_question == 0:

        back_button.config(
            state="disabled"
        )

    else:

        back_button.config(
            state="normal"
        )


# ==========================================
# NEXT QUESTION
# ==========================================

def next_question():

    global score
    global current_question


    # Make sure the user selected an answer.
    if choice.get() == -1:

        messagebox.showwarning(
            "No Answer",
            "Please select an answer."
        )

        return


    # Check if the user already answered
    # this question.
    if current_question < len(answers):

        # Get their old answer.
        old_answer = answers[current_question]


        # Remove the old score.
        score -= questions[current_question]["scores"][old_answer]


        # Store the new answer.
        answers[current_question] = choice.get()


    else:

        # Store the answer.
        answers.append(choice.get())


    # Add the score for the answer.
    score += questions[current_question]["scores"][choice.get()]


    # Move to the next question.
    current_question += 1


    # Check whether more questions remain.
    if current_question < len(questions):

        load_question()

    else:

        show_results()


# ==========================================
# PREVIOUS QUESTION
# ==========================================

def previous_question():

    global current_question


    # Make sure we are not on the first question.
    if current_question > 0:

        # Move backwards.
        current_question -= 1


        # Restore the previous answer.
        choice.set(
            answers[current_question]
        )


        # Load the question.
        load_question()


# ==========================================
# SHOW RESULTS
# ==========================================

def show_results():

    # Hide the quiz.
    quiz_frame.pack_forget()


    # Show the results.
    results_frame.pack(
        fill="both",
        expand=True
    )


    # Get the user's name.
    name = name_entry.get()


    # ======================================
    # CONSERVATIVE RESULT
    # ======================================

    if score <= 7:

        profile = "Conservative"


        explanation = (
            "You prefer lower levels of risk "
            "and may prioritise protecting your money."
        )


        recommendation = (
            "Savings Accounts\n"
            "Term Deposits\n"
            "Government Bonds"
        )


    # ======================================
    # MODERATE RESULT
    # ======================================

    elif score <= 11:

        profile = "Moderate"


        explanation = (
            "You are comfortable with some risk "
            "while still wanting some stability."
        )


        recommendation = (
            "Index Funds\n"
            "Balanced Funds\n"
            "Bonds"
        )


    # ======================================
    # GROWTH RESULT
    # ======================================

    else:

        profile = "Growth"


        explanation = (
            "You are comfortable taking more risk "
            "for potentially higher long-term returns."
        )


        recommendation = (
            "Growth ETFs\n"
            "Shares\n"
            "Global Index Funds"
        )


    # Display the results.
    result_label.config(
        text=(
            f"Well done, {name}!\n\n"

            f"Risk Profile: {profile}\n"

            f"Risk Score: {score}/15\n\n"

            f"{explanation}\n\n"

            f"Suggested Investments:\n"
            f"{recommendation}"
        )
    )


    # Save the result.
    save_result(
        name,
        profile,
        score
    )


# ==========================================
# SAVE RESULTS
# ==========================================

def save_result(
    name,
    profile,
    score
):

    # Open or create a CSV file.
    #
    # "a" means append, so new results
    # are added without deleting old results.
    with open(
        "investment_results.csv",
        "a",
        newline=""
    ) as file:

        # Create a CSV writer.
        writer = csv.writer(file)


        # Write the result to the file.
        writer.writerow([
            name,
            score,
            profile
        ])


# ==========================================
# INVESTMENT INFORMATION
# ==========================================

def show_investment_info():

    # Create a new window.
    info_window = tk.Toplevel(root)


    # Set the title.
    info_window.title(
        "Investment Information"
    )


    # Set the size.
    info_window.geometry(
        "550x500"
    )


    # Create a title.
    title = tk.Label(
        info_window,
        text="Investment Information",
        font=("Arial", 20)
    )

    title.pack(pady=20)


    # Store information about different
    # investment types.
    information = (

        "SAVINGS ACCOUNT\n"

        "Low risk and easy to access. "
        "Usually provides lower returns.\n\n"


        "TERM DEPOSIT\n"

        "Money is invested for a set period "
        "and earns interest.\n\n"


        "BONDS\n"

        "You lend money to a government or "
        "company and receive interest.\n\n"


        "INDEX FUNDS\n"

        "Invests in many companies at once, "
        "providing diversification.\n\n"


        "ETFs\n"

        "Funds that can be bought and sold "
        "on an exchange.\n\n"


        "SHARES\n"

        "You own part of a company. They can "
        "have higher returns but also higher risk."
    )


    # Display the information.
    information_label = tk.Label(
        info_window,
        text=information,
        font=("Arial", 11),
        justify="left",
        wraplength=480
    )


    information_label.pack(
        padx=20,
        pady=10
    )


# ==========================================
# RESTART QUIZ
# ==========================================

def restart():

    # Hide results.
    results_frame.pack_forget()


    # Clear the name.
    name_entry.delete(
        0,
        tk.END
    )


    # Show the starting screen.
    name_frame.pack(
        fill="both",
        expand=True
    )


# ==========================================
# NAME SCREEN
# ==========================================

name_frame = tk.Frame(root)


# Main title.
title = tk.Label(
    name_frame,
    text="Investment Recommendation Quiz",
    font=("Arial", 22)
)

title.pack(pady=40)


# Subtitle.
subtitle = tk.Label(
    name_frame,
    text="Find an investment profile based on your answers.",
    font=("Arial", 12)
)

subtitle.pack(pady=10)


# Name label.
name_label = tk.Label(
    name_frame,
    text="Enter your name:",
    font=("Arial", 14)
)

name_label.pack(pady=10)


# Text box for the user's name.
name_entry = tk.Entry(
    name_frame,
    font=("Arial", 14)
)

name_entry.pack()


# Start button.
start_button = tk.Button(
    name_frame,
    text="Start Quiz",
    command=start_quiz,
    font=("Arial", 12)
)

start_button.pack(pady=25)


# Show name screen.
name_frame.pack(
    fill="both",
    expand=True
)


# ==========================================
# QUIZ SCREEN
# ==========================================

quiz_frame = tk.Frame(root)


# Question progress.
progress_label = tk.Label(
    quiz_frame,
    text="",
    font=("Arial", 12)
)

progress_label.pack(pady=20)


# Question itself.
question_label = tk.Label(
    quiz_frame,
    text="",
    font=("Arial", 17),
    wraplength=550
)

question_label.pack(pady=25)


# Store selected answer.
choice = tk.IntVar(value=-1)


# Store radio buttons.
buttons = []


# Create three answer buttons.
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
        padx=200,
        pady=7
    )


    buttons.append(button)


# Navigation frame.
button_frame = tk.Frame(
    quiz_frame
)

button_frame.pack(
    pady=30
)


# Back button.
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


# Next button.
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

result_title.pack(pady=25)


# Result information.
result_label = tk.Label(
    results_frame,
    text="",
    font=("Arial", 13),
    justify="center",
    wraplength=600
)

result_label.pack(pady=20)


# Learn more button.
info_button = tk.Button(
    results_frame,
    text="Learn About Investments",
    command=show_investment_info
)

info_button.pack(pady=10)


# Retake button.
restart_button = tk.Button(
    results_frame,
    text="Retake Quiz",
    command=restart
)

restart_button.pack(pady=10)


# Disclaimer.
disclaimer = tk.Label(
    results_frame,
    text=(
        "For educational purposes only.\n"
        "This quiz does not provide professional financial advice."
    ),
    font=("Arial", 9)
)

disclaimer.pack(pady=20)


# ==========================================
# START PROGRAM
# ==========================================

# Start the Tkinter event loop.
root.mainloop()