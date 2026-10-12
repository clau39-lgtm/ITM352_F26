# Final version of the interactive quiz system
# Additional Requirements: 5 and 10
# Allow the user to choose a category for their questions
# Add a 50/50 feature (Removes 2 wrong answers, can only be used once per session)
# Coleman Lau
# Date: October 9, 2026

from string import ascii_lowercase
import random
import json
from pathlib import Path
import re

# This section of the code defines the function to choose a quiz category.
def choose_category(quiz_files):
    categories = [
        (re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", path.stem)
         .replace("_", " ") # Replace underscores with spaces for better readability
         .replace("-", " ") # Replace hyphens with spaces for better readability
         .title(), path)
        for path in quiz_files
    ]

    # This section of the code prints the available categories for the user to choose from.
    print("Available categories:")
    for number, (category, _) in enumerate(categories, start=1):
        print(f"{number}. {category}")

    # This section of the code handles the user's selection and returns the chosen quiz file path.
    while True:
        try:
            choice = int(input("Choose a category number: "))
        except ValueError:
            print("Please enter a number from the list.")
            continue

        # This makes sure that the user selects a valid category.
        if 1 <= choice <= len(categories):
            return categories[choice - 1][1]

        print(f"Please choose a number from 1 to {len(categories)}.")

# This section of the code loads the quiz files and allows the user to choose a category.
quiz_files = sorted(
    Path(__file__).resolve().parent.glob("*.json"),
    key=lambda path: path.stem.casefold()
)

# Checks for the presence of any quiz category JSON files.
# If no files are found, the program will raise a FileNotFoundError.
if not quiz_files:
    raise FileNotFoundError("No quiz category JSON files were found.")


# This section of the code loads the chosen quiz file and parses its JSON content.
quiz_file = choose_category(quiz_files)
try:
    with quiz_file.open("r", encoding="utf-8") as question_file:
        questions = json.load(question_file)
except json.JSONDecodeError as error:
    raise ValueError(f"{quiz_file.name} does not contain valid JSON.") from error

if not isinstance(questions, dict) or not questions:
    raise ValueError(
        f"{quiz_file.name} must contain a non-empty object of questions and answers."
    )


NUM_QUESTIONS_PER_QUIZ = 5

def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

# This section of the code defines the function to handle the user's answer selection, including the use of the 50/50 lifeline.
def get_answer(alternative_answers, correct_answer, can_use_fifty_fifty):
    lifeline_used = False
    displayed_answers = alternative_answers
    wrong_indices = [
        index for index, answer in enumerate(alternative_answers)
        if answer != correct_answer
    ]

    # This section of the code checks if the user can use the 50/50 lifeline and prompts them accordingly.
    if can_use_fifty_fifty and len(wrong_indices) >= 2:
        while (use_lifeline := input(
            "Use 50/50 to remove two wrong answers? (y/n): "
        ).strip().lower()) not in {"y", "n"}:
            print("Please enter y or n.")

        if use_lifeline == "y":
            removed_indices = set(random.sample(wrong_indices, k=2))
            displayed_answers = [
                answer for index, answer in enumerate(alternative_answers)
                if index not in removed_indices
            ]
            lifeline_used = True
    elif can_use_fifty_fifty:
        print("50/50 is unavailable because this question has fewer than two wrong answers.")

    labeled_answers = dict(zip(ascii_lowercase, displayed_answers))

    for label, answer in labeled_answers.items():
        print(f"{label}. {answer}")

    while (answer_label := input("Choice? ").strip().lower()) not in labeled_answers:
        print(f"Invalid choice. Please select one of {', '.join(labeled_answers.keys())}")

    return labeled_answers[answer_label], lifeline_used


def ask_question(question, alternative_answers, can_use_fifty_fifty):
    correct_answer = alternative_answers[0]
    ordered_alternative_answers = random.sample(alternative_answers, k=len(alternative_answers))
    answer, lifeline_used = get_answer(
        ordered_alternative_answers, correct_answer, can_use_fifty_fifty
    )
    if answer == correct_answer:
            print("Correct!")
            return 1, lifeline_used
    else:
        print(f"Incorrect! The correct answer is '{correct_answer!r}', not {answer!r}.")
        return 0, lifeline_used


# Main program logic starts here
question = prepare_questions(questions, NUM_QUESTIONS_PER_QUIZ)

num_correct = 0
fifty_fifty_used = False

# Main Loop
for num, (question, answers) in enumerate(question, start=1):
    print(f"\nQuestion {num}: {question}")
    score, lifeline_used = ask_question(
        question, answers, can_use_fifty_fifty=not fifty_fifty_used
    )
    num_correct += score
    fifty_fifty_used = fifty_fifty_used or lifeline_used
    
print(f"\nYou got {num_correct} questions correct!")