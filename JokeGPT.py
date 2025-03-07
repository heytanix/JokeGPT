import logging
from flask import Flask, jsonify
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv
import os
import random

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Get API key from environment variables
api_key = os.getenv("API_KEY")
if not api_key:
    logging.error("API_KEY not found in environment variables.")
    raise ValueError("API_KEY not found in environment variables.")

# Initialize GenAI client
client = genai.Client(api_key=api_key)

@app.route('/get_joke', methods=['GET'])
def fetch_joke():
    try:
        logging.info('Received request for a joke...')
        joke = get_joke()
        logging.info(f'Joke fetched: {joke}')
        return jsonify({"joke": joke})
    except Exception as e:
        logging.error(f"Error occurred while fetching joke: {e}")
        return jsonify({"error": str(e)}), 500

# Function to fetch a random joke
def get_joke():
    try:
        topics = [
            "animals", "sports", "food", "technology", "travel",
            "music", "movies", "science", "history", "books"
        ]
        selected_topic = random.choice(topics)
        logging.info(f"Selected topic for joke: {selected_topic}")
        
        prompt = f"Tell me a funny joke about {selected_topic} in a complete sentence."
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=f"{prompt} | The rules are: 1. The joke should be funny, 2. The joke should not contain dark humor, 3. The joke should not be offensive, 4. The joke should not contain NSFW content"
        )
        
        logging.debug(f"Raw response from GenAI: {response.text}")
        
        if response and response.text:
            jokes = response.text.strip().split('\n')
            unique_jokes = list(set(jokes))
            logging.info(f"Unique jokes generated: {unique_jokes}")
            return random.choice(unique_jokes).strip() if unique_jokes else "No joke found."
        else:
            raise ValueError("No valid joke returned from GenAI.")
        
    except Exception as e:
        logging.error(f"Error generating joke: {e}")
        raise

if __name__ == "__main__":
    logging.info("Starting Flask application...")
    app.run(debug=True)
