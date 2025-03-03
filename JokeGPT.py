from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv
import os
import random

# Loading environment variables from .env
load_dotenv()

app = Flask(__name__, static_folder='.')  # Serving static files from the current directory
CORS(app)  # Enable CORS for all routes

# Initialize the GenAI client with API key
api_key = os.getenv("API_KEY")
client = genai.Client(api_key=api_key)

# Function to get a joke
def get_joke():
    topics = ["animals", "sports", "food", "technology", "travel", "music", "movies", "science", "history", "books"]
    selected_topic = random.choice(topics)
    prompt = f"Tell me a funny joke about {selected_topic} in a complete sentence."

    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=f"{prompt} | The rules are: 1. The joke should be funny, 2. The joke should not contain dark humor, 3. The joke should not be offensive, 4. The joke should not contain NSFW content"
    )

    jokes = response.text.strip().split('\n')
    unique_jokes = list(set(jokes))  # Remove duplicates
    return random.choice(unique_jokes).strip() if unique_jokes else "No joke found."

# Route to serve index.html
@app.route('/')
def home():
    return send_from_directory(os.getcwd(), 'index.html')

# Route to fetch the joke
@app.route('/get_joke', methods=['GET'])
def fetch_joke():
    try:
        joke = get_joke()
        return jsonify({"joke": joke})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Serve static files (like styles.css)
@app.route('/<path:filename>', methods=['GET'])
def serve_static(filename):
    return send_from_directory(os.getcwd(), filename)

if __name__ == "__main__":
    app.run(debug=True)
