🧠 CLI Quiz Application
A dynamic Command Line Interface (CLI) quiz application built with Python. This tool reads questions from a JSON file, shuffles them to ensure a unique experience every time, and shuffles the answer options to keep the user on their toes!
🚀 Features
Data-Driven: Questions are stored in a separate questions.json file, making it easy to add or edit content without touching the code.
Double Shuffling:
Shuffles the order of questions.
Shuffles the order of options within each question.
Robust Input Handling: Uses try-except blocks to prevent the program from crashing if a user enters a letter instead of a number.
Real-time Feedback: Tells the user immediately if they were correct or wrong and reveals the correct answer upon a mistake.
Score Tracking: Calculates and displays the final score at the end of the session.
🛠️ Technology Used
Python 
JSON: For persistent question storage.
Random Module: For randomization of data.
📂 Project Structure
main.py: The core logic of the quiz.
questions.json: The database containing questions, options, and correct answers.
README.md: Project documentation.
📥 Getting Started
Clone the repository:
code
Bash
git clone https://github.com/dhusniddinov123/Quiz-Game.git
Navigate to the folder:
code
Bash
cd your-repo-name
Ensure you have a questions.json file in the same directory.
Run the quiz:
code
Bash
python main.py
