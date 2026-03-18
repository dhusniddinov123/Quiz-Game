import os
import json 
import random

def load_questions(filename="questions.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

def run_quiz(questions):
    if not questions:
        print("No questions ")
        return
    
    score = 0
    
    for question in questions:
        print(f"\n{question['question']}")

        new_options = random.sample(question["options"], len(question["options"]))
        for i,option in enumerate(new_options, start=1):
            print(f"{i}) {option}")

        try:
            choice = int(input("Your answer in numbers: "))

            if 1 <= choice <= len(new_options):
                selected_option = new_options[choice-1]

                if selected_option == question["answer"]:
                    print("Correct :)")
                    score += 1
                else:
                    print(f"Wrong :( \nCorrect answer was {question['answer']}")
            else:
                print("Invalid choice number")
                
        except ValueError:
            print("Invalid input! Please enter a number.")

    print(f"\nFinal score: {score}/{len(questions)}")


def main():
    questions = load_questions()
    random.shuffle(questions)
    run_quiz(questions)

if __name__ == "__main__":
    main()