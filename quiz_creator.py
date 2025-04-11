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
        
        correct_answer = input("\n✅ Enter the correct answer (a, b, c, d): ").lower()
        while correct_answer not in ['a', 'b', 'c', 'd']:
            print("❌ Invalid option. Please enter a, b, c, or d.")
            correct_answer = input("✅ Enter the correct answer (a, b, c, d): ").lower()
        
        # Write the question and answers to the file
        with open(output_file, "a") as file:
            file.write(f"Question: {question}\n")
            for i, option in enumerate(['a', 'b', 'c', 'd']):
                file.write(f("Option {option}: {choices[i]}\n"))
            file.write(f"Correct Answer: {correct_answer}\n")
            file.write("-" * 50 + "\n")
            
        questions_added += 1
        print(f"\n🎉 Question added succesfully!")
        
        # Ask if the user wants to add another question
        another_question = input("\n➕ Do you want to add another question? (yes/no): ").lower()
        if another_question != 'yes':
            print("\n✨ Thank you for using the Quiz Creator!")
            print(f"📂 Quiz data saved to: {os.path.abspath(output_file)}")
            print(f"📊 Total questions added: {questions_added}")
            break

main()