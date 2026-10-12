# Interactive quiz system, fifth version
# Make a dictionary with the questions and correct answers.
# Allow the user to choose the option by its label.
# Improve the look and usability. Keep track of correct answers.

from string import ascii_lowercase

questions = {
    "What is the capital of France?": ["Paris", "Lyon", "Marseille", "Toulouse"],
    "What is the capital of Germany?": ["Berlin", "Munich", "Hamburg", "Cologne"],
    "What is the capital of Japan?": ["Tokyo", "Kyoto", "Osaka", "Nagoya"],
    "The Last Supper was painted by which artist?": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"]
}

correct_answers = 0

for num, (question, answers) in enumerate(questions.items(), start=1):
    correct_answer = answers[0]
    print(f"\nQuestion {num}: {question}")
    
    sorted_answers = sorted(answers)
    labeled_answers = dict(zip(ascii_lowercase, sorted_answers))

    for label, answer in labeled_answers.items():
        print(f"{label}. {answer}")
        
    answer_label = input("Choice? ").lower()
    answer = labeled_answers.get(answer_label)

    if answer == correct_answer:
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Incorrect! The correct answer is '{correct_answer!r}', not {answer!r}.")

print(f"\nYou got {correct_answers} out of {len(questions)} questions correct.")