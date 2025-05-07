import os
import sys
from colorama import Fore, Style
import random

# File path for the quiz data question
quiz_question = "quiz_questions.txt"

# Load the quiz questions from the file
def load_quiz_questions():
    # Check if the quiz question file exists
    if not os.path.exists(quiz_question):
        print(Fore.RED + "❌ Error: The file {quiz_question} does not exist." + Style.RESET_ALL)
        sys.exit(1)
        
# Open the quiz question file in read mode
    with open(quiz_question, 'r') as file:
        lines = file.readlines()
        
# Initialize variables to store question data
    question = None
    options = {}
    correct_answer = None
    questions = []  # List to store all questions
    
# Iterate through each line in the file to extract question data
    for line in lines:
        line = line.strip()
        if line.startswith("Question:"):
            question = line.split("Question:")[1].strip()
        elif line.startswith("Option"):
            option_key, option_value = line.split(":")
            options[option_key.split()[1].strip()] = option_value.strip()
        elif line.startswith("Correct Answer:"):
            correct_answer = line.split("Correct Answer:")[1].strip()
        elif line.startswith("-" * 50):  # End of a question block
            # If all components of a question are present, add it to the list
            if question and options and correct_answer:
                questions.append({
                    "question": question,
                    "options": options,
                    "correct_answer": correct_answer
                })
            # Reset for the next question
            question = None
            options = {}
            correct_answer = None

    return questions

def ask_question(question_data):
    # Display the question
    print(Fore.CYAN + "\n❓ " + question_data["question"] + Style.RESET_ALL)