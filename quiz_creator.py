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