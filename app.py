from flask import Flask, render_template, request
from webhook_ingest import ingest_stories_to_local_db
from chat_vector_search import search_chat_input
from score_checker import score_result
import json

app = Flask(__name__)

# Load stories from JSON file
with open("stories.json", "r") as file:
    stories = json.load(file)

# Step 1: Ingest stories
ingest_stories_to_local_db(stories)

@app.route("/")
def index():
    return render_template("input_form.html")

@app.route("/process_input", methods=["POST"])
def process_input():
    user_input = request.form["user_input"]

    # Step 3: Search similar story
    search_results = search_chat_input(user_input)

    # Step 4: Score the match
    score = score_result(user_input, search_results)

    # Return results to the user
    top_match = search_results[0]['metadata']['text'] if search_results else 'No match'
    return f"""
    <h1>Results</h1>
    <p><strong>User Input:</strong> {user_input}</p>
    <p><strong>Top Match:</strong> {top_match}</p>
    <p><strong>Similarity Score:</strong> {score}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
