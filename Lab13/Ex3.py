"""Display a random wholesome meme."""

import requests
from flask import Flask, render_template_string

app = Flask(__name__)

MEME_API_URL = "https://meme-api.com/gimme/wholesomememes"

PAGE_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <title>Memes'R'Us</title>
    <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=0.8">
    <meta http-equiv="refresh" content="10; url=http://127.0.0.1:5000">
    <style>
        body { font-family: sans-serif; margin: 2rem auto; max-width: 800px; text-align: center; }
        img { height: auto; max-height: 70vh; max-width: 100%; }
    </style>
</head>
<body>
    <h1>Memes'R'Us</h1>
    {% if error %}
        <p>{{ error }}</p>
    {% else %}
        <img src="{{ meme_url }}" alt="{{ title }}">
        <p>{{ title }}</p>
        <p>Source: r/{{ subreddit }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/")
def index():
    response = requests.request("GET", MEME_API_URL, timeout=10)
    response.raise_for_status()
    meme = response.json()
    
    meme_url = meme.get("url")
    subreddit = meme.get("subreddit")

    return render_template_string(
        PAGE_TEMPLATE,
        meme_url=meme_url,
        subreddit=subreddit,
        title=meme.get("title", "Wholesome meme"),
        error=None,
    )


if __name__ == "__main__":
    app.run()