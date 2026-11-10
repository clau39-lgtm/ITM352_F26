# Save the dictionary of quiz questions to a JSON file
import json

questions = {
    "What is the capital of France?": ["Paris", "Lyon", "Marseille", "Toulouse"],
    "What is the capital of Germany?": ["Berlin", "Munich", "Hamburg", "Cologne"],
    "What is the capital of Japan?": ["Tokyo", "Kyoto", "Osaka", "Nagoya"],
    "The Last Supper was painted by which artist?": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"],
    "Which NHL player has the most career points?": ["Wayne Gretzky", "Gordie Howe", "Mario Lemieux", "Jaromir Jagr"],
    "Which classic novel opens with the line 'Call me Ishmael'?": ["Moby Dick", "The Great Gatsby", "To Kill a Mockingbird", "1984"],
    "What is the largest planet in our solar system?": ["Jupiter", "Saturn", "Neptune", "Earth"]
}

filename = "quiz_questions.json"

# Open the file in write mode and save the questions dictionary as JSON
with open(filename, 'w') as file:
    json.dump(questions, file, indent=2)

print(f"Quiz questions saved to {filename}")