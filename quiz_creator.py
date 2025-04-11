import os

def main():
    output_file = "quiz_questions.txt"
    
    # Check if the file exists; if not, write the header
    if not os.path.exists(output_file):
        with open(output_file, "w") as file:
            file.write("Quiz Questions\n")
            file.write("=" * 50 + "\n")
            
    print("=" * 50)
    print("🎉 Welcome to the Quiz Creator! 🎉")
    print("=" * 50)