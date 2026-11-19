# Flask version of the category-based quiz game in Assignment1.

import json
import os
import random
import re
import secrets
from pathlib import Path

from flask import (
    Flask,
    flash,
    get_flashed_messages,
    redirect,
    render_template_string,
    request,
    session,
    url_for,
)

QUIZ_DIR = Path(__file__).resolve().parents[1] / "Assignment1"
NUM_QUESTIONS_PER_QUIZ = 5

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY", secrets.token_hex(32))

BASE_STYLE = """
<style>
    * { box-sizing: border-box; }
    body {
        background: #f4f7fb;
        color: #202b3c;
        font-family: sans-serif;
        line-height: 1.5;
        margin: 0;
        padding: clamp(1rem, 4vw, 2.5rem) 1rem;
    }
    main { background: #fff; border-radius: 0.75rem; margin: 0 auto; max-width: 700px; padding: clamp(1.25rem, 5vw, 2.5rem); }
    h1 { color: #23395d; margin-top: 0; }
    fieldset { border: 0; margin: 1rem 0; padding: 0; }
    legend { font-weight: 600; }
    .option { align-items: flex-start; display: flex; gap: 0.65rem; margin: 0.75rem 0; padding: 0.25rem 0; }
    .option input { flex: 0 0 auto; margin-top: 0.35rem; }
    .message, .explanation { background: #f0f4f8; border-left: 4px solid #4267a5; margin: 1rem 0; padding: 0.75rem 1rem; }
    .correct { border-left-color: #27834a; }
    .incorrect { border-left-color: #b23b3b; }
    button, select {
        border: 1px solid #64748b;
        border-radius: 0.35rem;
        font: inherit;
        min-height: 2.75rem;
        padding: 0.55rem 0.8rem;
    }
    button { background: #23395d; color: #fff; cursor: pointer; margin: 0.5rem 0.5rem 0.5rem 0; }
    button:hover { background: #172943; }
    a { color: #23395d; }
    :focus-visible { outline: 3px solid #e3a72f; outline-offset: 3px; }
    .review-item { border-top: 1px solid #d8e0ea; margin-top: 1.5rem; padding-top: 1rem; }
    @media (max-width: 480px) {
        body { padding: 0.75rem; }
        main { border-radius: 0.5rem; padding: 1.15rem; }
        form button { margin-right: 0; width: 100%; }
        select { max-width: 100%; width: 100%; }
    }
</style>
"""

HOME_TEMPLATE = """
<!doctype html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Quiz Game</title>
{{ style|safe }}</head>
<body>
<main>
    <h1>Quiz Game</h1>
    <p>Choose a category to start a quiz of up to five questions.</p>
    {% for message in messages %}<p class="message">{{ message }}</p>{% endfor %}
    {% if categories %}
    <form action="{{ url_for('start') }}" method="post">
        <label for="category">Quiz category</label>
        <select id="category" name="category" required>
            {% for filename, label in categories %}
            <option value="{{ filename }}">{{ label }}</option>
            {% endfor %}
        </select>
        <button type="submit">Start Quiz</button>
    </form>
    {% else %}
    <p>No quiz category JSON files were found in {{ quiz_dir }}.</p>
    {% endif %}
</main>
</body>
</html>
"""

QUIZ_TEMPLATE = """
<!doctype html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Quiz Game</title>
{{ style|safe }}</head>
<body>
<main>
    <h1>{{ category }}</h1>
    {% for message in messages %}<p class="message">{{ message }}</p>{% endfor %}
    <p>Question {{ question_number }} of {{ total_questions }}</p>
    <h2>{{ question }}</h2>
    <form action="{{ url_for('quiz') }}" method="post">
        <fieldset>
            <legend>Choose an answer</legend>
            {% for option in options %}
            <label class="option">
                <input type="radio" name="choice" value="{{ loop.index0 }}" required>
                {{ option }}
            </label>
            {% endfor %}
        </fieldset>
        <button type="submit" name="action" value="answer">Submit Answer</button>
    </form>
    {% if not lifeline_used and wrong_options_available %}
    <form action="{{ url_for('quiz') }}" method="post">
        <button type="submit" name="action" value="lifeline">Use 50/50 Lifeline</button>
    </form>
    {% elif lifeline_used %}
    <p>Your 50/50 lifeline has been used.</p>
    {% endif %}
    <p>Score: {{ score }}</p>
</main>
</body>
</html>
"""

FEEDBACK_TEMPLATE = """
<!doctype html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Answer Review</title>
{{ style|safe }}</head>
<body>
<main>
    <h1>Answer Review</h1>
    <p>Question {{ question_number }} of {{ total_questions }}: {{ question }}</p>
    <p class="{{ 'correct' if is_correct else 'incorrect' }} explanation" role="status">
        {% if is_correct %}Correct!{% else %}Not quite. The correct answer is {{ correct_answer }}.{% endif %}
    </p>
    <section class="explanation" aria-labelledby="explanation-title">
        <h2 id="explanation-title">Explanation</h2>
        <p>{{ explanation }}</p>
    </section>
    <form action="{{ url_for('feedback') }}" method="post">
        <button type="submit">Continue</button>
    </form>
</main>
</body>
</html>
"""

RESULT_TEMPLATE = """
<!doctype html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Quiz Results</title>
{{ style|safe }}</head>
<body>
<main>
    <h1>Quiz Complete!</h1>
    {% for message in messages %}<p class="message">{{ message }}</p>{% endfor %}
    <p>You got {{ score }} out of {{ total_questions }} questions correct.</p>
    {% if missed_questions %}
    <h2>Review missed questions</h2>
    <p>Here are the questions you missed and why their correct answers are right.</p>
    {% for item in missed_questions %}
    <section class="review-item">
        <h3>{{ loop.index }}. {{ item.question }}</h3>
        <p>Your answer: {{ item.user_answer }}</p>
        <p>Correct answer: {{ item.correct_answer }}</p>
        <div class="explanation">
            <strong>Explanation</strong>
            <p>{{ item.explanation }}</p>
        </div>
    </section>
    {% endfor %}
    {% else %}
    <p>You answered every question correctly. Great work!</p>
    {% endif %}
    <a href="{{ url_for('index') }}">Play Again</a>
</main>
</body>
</html>
"""


def get_categories():
    categories = []
    for path in sorted(QUIZ_DIR.glob("*.json"), key=lambda item: item.stem.casefold()):
        label = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", path.stem)
        label = label.replace("_", " ").replace("-", " ").title()
        categories.append((path.name, label))
    return categories


def load_questions(path):
    try:
        with path.open("r", encoding="utf-8") as question_file:
            data = json.load(question_file)
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"Could not load {path.name}: {error}") from error

    if not isinstance(data, dict) or not data:
        raise ValueError(f"{path.name} must contain questions and answer lists.")

    questions = {}
    for question, value in data.items():
        # To add an explanation, use {"answers": [...], "explanation": "..."} in the JSON.
        if isinstance(value, list):
            answers = value
            explanation = "No explanation has been added for this question yet."
        elif isinstance(value, dict):
            answers = value.get("answers")
            explanation = value.get(
                "explanation", "No explanation has been added for this question yet."
            )
        else:
            answers = None
            explanation = None

        if (
            not isinstance(question, str)
            or not isinstance(answers, list)
            or not answers
            or not all(isinstance(answer, str) for answer in answers)
            or not isinstance(explanation, str)
        ):
            raise ValueError(f"{path.name} contains an invalid question or answer list.")
        questions[question] = {"answers": answers, "explanation": explanation}

    return questions


@app.route("/")
def index():
    return render_template_string(
        HOME_TEMPLATE,
        categories=get_categories(),
        messages=list(get_flashed_messages()),
        quiz_dir=QUIZ_DIR,
        style=BASE_STYLE,
    )


@app.route("/start", methods=["POST"])
def start():
    categories = dict(get_categories())
    filename = request.form.get("category", "")
    if filename not in categories:
        flash("Please choose a valid quiz category.")
        return redirect(url_for("index"))

    try:
        questions = load_questions(QUIZ_DIR / filename)
    except ValueError as error:
        flash(str(error))
        return redirect(url_for("index"))

    selected_questions = random.sample(
        list(questions.items()),
        k=min(NUM_QUESTIONS_PER_QUIZ, len(questions)),
    )
    session["quiz"] = []
    for question, question_data in selected_questions:
        answers = question_data["answers"]
        session["quiz"].append(
            {
                "question": question,
                "correct_answer": answers[0],
                "options": random.sample(answers, k=len(answers)),
                "explanation": question_data["explanation"],
            }
        )
    session["category"] = categories[filename]
    session["question_index"] = 0
    session["score"] = 0
    session["lifeline_used"] = False
    session["missed_questions"] = []
    session.pop("feedback", None)
    return redirect(url_for("quiz"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    questions = session.get("quiz")
    if not questions:
        return redirect(url_for("index"))

    question_index = session["question_index"]
    if session.get("feedback"):
        return redirect(url_for("feedback"))
    if question_index >= len(questions):
        return redirect(url_for("result"))

    current = questions[question_index]
    if request.method == "POST":
        action = request.form.get("action")
        if action == "lifeline":
            wrong_indices = [
                index for index, option in enumerate(current["options"])
                if option != current["correct_answer"]
            ]
            if session["lifeline_used"]:
                flash("Your 50/50 lifeline has already been used.")
            elif len(wrong_indices) < 2:
                flash("The 50/50 lifeline is unavailable for this question.")
            else:
                removed_indices = set(random.sample(wrong_indices, k=2))
                current["options"] = [
                    option for index, option in enumerate(current["options"])
                    if index not in removed_indices
                ]
                session["quiz"] = questions
                session["lifeline_used"] = True
            return redirect(url_for("quiz"))

        if action == "answer":
            choice = request.form.get("choice", "")
            if not choice.isdigit() or int(choice) >= len(current["options"]):
                flash("Choose one of the listed answers.")
                return redirect(url_for("quiz"))

            answer = current["options"][int(choice)]
            is_correct = answer == current["correct_answer"]
            if is_correct:
                session["score"] += 1
            else:
                missed_questions = session.get("missed_questions", [])
                missed_questions.append(
                    {
                        "question": current["question"],
                        "user_answer": answer,
                        "correct_answer": current["correct_answer"],
                        "explanation": current["explanation"],
                    }
                )
                session["missed_questions"] = missed_questions
            session["feedback"] = {
                "question": current["question"],
                "question_number": question_index + 1,
                "is_correct": is_correct,
                "correct_answer": current["correct_answer"],
                "explanation": current["explanation"],
            }
            session["question_index"] += 1
            return redirect(url_for("feedback"))

        flash("Please submit an answer or use the 50/50 lifeline.")
        return redirect(url_for("quiz"))

    return render_template_string(
        QUIZ_TEMPLATE,
        category=session.get("category", "Quiz"),
        question=current["question"],
        question_number=question_index + 1,
        total_questions=len(questions),
        options=current["options"],
        lifeline_used=session["lifeline_used"],
        wrong_options_available=sum(
            option != current["correct_answer"] for option in current["options"]
        ) >= 2,
        score=session["score"],
        messages=list(get_flashed_messages()),
        style=BASE_STYLE,
    )


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    questions = session.get("quiz")
    answer_feedback = session.get("feedback")
    if not questions or not answer_feedback:
        return redirect(url_for("quiz") if questions else url_for("index"))

    if request.method == "POST":
        session.pop("feedback", None)
        return redirect(
            url_for("result")
            if session["question_index"] >= len(questions)
            else url_for("quiz")
        )

    return render_template_string(
        FEEDBACK_TEMPLATE,
        **answer_feedback,
        total_questions=len(questions),
        style=BASE_STYLE,
    )


@app.route("/result")
def result():
    questions = session.get("quiz")
    if not questions or session.get("question_index", 0) < len(questions):
        return redirect(url_for("index"))
    return render_template_string(
        RESULT_TEMPLATE,
        score=session.get("score", 0),
        total_questions=len(questions),
        missed_questions=session.get("missed_questions", []),
        messages=list(get_flashed_messages()),
        style=BASE_STYLE,
    )


if __name__ == "__main__":
    app.run()