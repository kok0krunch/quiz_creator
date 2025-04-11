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
    
    questions_added = 0 # Counter for the number of questions added
    
    while True:
        print("\nLet's create a new quiz question!")
        question = input("📝 Enter the question: ").title()
        
        choices = []
        print("\n💡 Enter options for answers (a, b, c, d):")
        for option in ['a', 'b', 'c', 'd']:
            choice = input(f"   ➡ Option {option}: ").title()
            choices.append(choice)