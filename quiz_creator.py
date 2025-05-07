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
    # Display the options
    for key, value in question_data["options"].items():
        print(Fore.YELLOW + f"   {key}: {value}" + Style.RESET_ALL)
    # Prompt the user for their answer
    user_answer = input(Fore.YELLOW + "👉 Your answer (a, b, c, d): " + Style.RESET_ALL).lower()
    # Check if the user's answer is correct
    if user_answer == question_data["correct_answer"]:
        print(Fore.GREEN + "🎉 Correct! Great job!" + Style.RESET_ALL)  # Correct answer feedback
        return True
    else:
        # Incorrect answer feedback with the correct answer displayed
        print(Fore.RED + f"❌ Wrong! The correct answer was: {question_data['correct_answer']}" + Style.RESET_ALL)
        return False
    
def main_menu():
    # Load questions from the file
    questions = load_quiz_questions()
    if not questions:
        print(Fore.RED + "❌ No questions available. Exiting the quiz." + Style.RESET_ALL)
        sys.exit(1)
        
    # Display the main menu
    print(Fore.MAGENTA + "🎮 Welcome to the Quiz Game! 🎮" + Style.RESET_ALL)
    print("=" * 50)
    print("1. Start Quiz")
    print("2. Rules of the Quiz")
    print("3. Exit")
    print("=" * 50)
    choice = input(Fore.YELLOW + "👉 Choose an option (1-3): " + Style.RESET_ALL)