# Interactive quiz system, fourth version
# Make a dictionary with the questions and correct answers.
# Allow the user to choose the option by its label.

questions = {
    "What is the capital of France?": ["Paris", "Lyon", "Marseille", "Toulouse"],
    "What is the capital of Germany?": ["Berlin", "Munich", "Hamburg", "Cologne"],
    "What is the capital of Japan?": ["Tokyo", "Kyoto", "Osaka", "Nagoya"],
    "The Last Supper was painted by which artist?": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"]
}

for question, answers in questions.items():
    correct_answer = answers[0]
    sorted_answers = sorted(answers)

    for label, answer in enumerate(sorted_answers, start=1):
        print(f"{label}. {answer}")
        
    answerLabel = int(input(f"{question} "))
    answer = sorted_answers[answerLabel - 1]
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect! The correct answer is '{correct_answer!r}', not '{answer!r}'")