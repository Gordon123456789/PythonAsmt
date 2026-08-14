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


