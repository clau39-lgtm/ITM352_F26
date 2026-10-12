# Interactive quiz system, sixth version
# Make a dictionary with the questions and correct answers.
# Allow the user to choose the option by its label.
# Improve the look and usability. Keep track of correct answers.
# Randomize the order of answers for each question and the order of the answers for each question.

from string import ascii_lowercase
import random

questions = {
    "What is the capital of France?": ["Paris", "Lyon", "Marseille", "Toulouse"],
    "What is the capital of Germany?": ["Berlin", "Munich", "Hamburg", "Cologne"],
    "What is the capital of Japan?": ["Tokyo", "Kyoto", "Osaka", "Nagoya"],
    "The Last Supper was painted by which artist?": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"],
    "Which NHL player has the most career points?": ["Wayne Gretzky", "Gordie Howe", "Mario Lemieux", "Jaromir Jagr"],
    "Which classic novel opens with the line 'Call me Ishmael'?": ["Moby Dick", "The Great Gatsby", "To Kill a Mockingbird", "1984"]
}

NUM_QUESTIONS_PER_QUIZ = 5

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(questions))
selected_questions = random.sample(list(questions.items()), k=num_questions)

correct_answers = 0

for num, (question, answers) in enumerate(selected_questions, start=1):
    correct_answer = answers[0]
    print(f"\nQuestion {num}: {question}")
    
    sorted_answers = sorted(answers)
    labeled_answers = dict(zip(ascii_lowercase, random.sample(sorted_answers, k=len(sorted_answers))))

    for label, answer in labeled_answers.items():
        print(f"{label}. {answer}")

    while (answer_label := input("Choice? ").lower()) not in labeled_answers:
        print(f"Invalid choice. Please select one of {', '.join(labeled_answers.keys())}")
    
    answer = labeled_answers.get(answer_label)

    if answer == correct_answer:
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Incorrect! The correct answer is '{correct_answer!r}', not {answer!r}.")

print(f"\nYou got {correct_answers} out of {len(selected_questions)} questions correct.")