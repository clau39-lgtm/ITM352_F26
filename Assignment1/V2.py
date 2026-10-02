# Interactive quiz system, second version
# Make a list with the questions and answers

questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the capital of Germany?", "answer": "Berlin"},
    {"question": "What is the capital of Japan?", "answer": "Tokyo"}
]

for question, correct_answer in questions:
    answer = input(f"{question} ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect! The correct answer is {correct_answer}")