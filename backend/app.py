from flask import Flask, render_template, jsonify
import random

app = Flask(__name__, template_folder="../frontend")

books = [
    {"title": "Atomic Habits", "author": "James Clear", "genre": "Self-help"},
    {"title": "The Alchemist", "author": "Paulo Coelho", "genre": "Fiction"},
    {"title": "Deep Work", "author": "Cal Newport", "genre": "Productivity"},
    {"title": "Sapiens", "author": "Yuval Noah Harari", "genre": "History"},
    {"title": "Python Crash Course", "author": "Eric Matthes", "genre": "Programming"},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/book/suggest")
def suggest_book():
    return jsonify(random.choice(books))

if __name__ == "__main__":
    app.run(debug=False)

