# Application to manage the quiz webApp
# Name: Coleman Lau
# Date: Nov. 13, 2026

from flask import Flask, render_template, request, redirect, url_for

# Global variables
score = 0
questionNumber = 0
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Madrid", "London", "Berlin", "Paris"],
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "6", "5", "4"],
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Saturn", "Jupiter"],
    }
]

maxQuestions = len(questions)

app = Flask(__name__)

@app.route('/')
def index():
    global score, questionNumber
    score = 0
    questionNumber = 0
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global score, questionNumber, maxQuestions, questions

    if request.method == 'POST':
        # Capture the answer from the form
        answer = request.form.get('answer')

        # Check if the answer is correct
        if answer == questions[questionNumber]['options'][3]:
            score += 1

        # Move to next question
        questionNumber += 1

        # Check if the quiz is over
        if questionNumber < maxQuestions:
            # Render the next question
            return render_template('quiz.html', question=questions[questionNumber], questionNumber=questionNumber, options=questions[questionNumber]['options'])
        else:
            return render_template('result.html', score=score, maxQuestions=maxQuestions)

@app.route('/result')
def result():
    # Display the final score
    global score, maxQuestions
    return render_template('result.html', score=score, maxQuestions=maxQuestions)

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()