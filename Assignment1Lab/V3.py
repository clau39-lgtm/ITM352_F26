# Interactive quiz system, third version
# Make a dictionary with the questions and correct answers.

questions = {
    "What is the capital of France?": ["Paris", "Lyon", "Marseille", "Toulouse"],
    "What is the capital of Germany?": ["Berlin", "Munich", "Hamburg", "Cologne"],
    "What is the capital of Japan?": ["Tokyo", "Kyoto", "Osaka", "Nagoya"],
    "The Last Supper was painted by which artist?": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"]
}

for question, answers in questions.items():
    correct_answer = answers[0]
    for answer in answers:
        print(f"- {answer}")
        
    answer = input(f"{question} ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect! The correct answer is {correct_answer}")