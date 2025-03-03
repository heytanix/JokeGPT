import logging
from flask import Flask, jsonify
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv
import os
import random

# Set up logging for better error tracking
logging.basicConfig(level=logging.DEBUG)

# Load environment variables from the .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Get the API key from the environment variable
api_key = os.getenv("API_KEY")  # Ensure your API_KEY is correctly set in Vercel environment variables
if not api_key:
    logging.error("API_KEY not found in environment variables.")
    raise ValueError("API_KEY not found in environment variables.")

# Initialize the GenAI client with the API key
client = genai.Client(api_key=api_key)

@app.route('/get_joke', methods=['GET'])
def fetch_joke():
    try:
        logging.info('Received request for a joke...')
        joke = get_joke()  # Call the get_joke function to fetch a random joke
        logging.info(f'Joke fetched: {joke}')
        return jsonify({"joke": joke})  # Return the joke as a JSON response
    except Exception as e:
        logging.error(f"Error occurred while fetching joke: {e}")
        return jsonify({"error": str(e)}), 500  # Return error message in case of failure

def get_joke():
    try:
        # List of possible topics for jokes
        topics = [
            "animals", "sports", "food", "technology", "travel",
            "music", "movies", "science", "history", "books"
        ]
        
        # Randomly select a topic from the list
        selected_topic = random.choice(topics)
        logging.info(f"Selected topic for joke: {selected_topic}")
        
        # Generate a prompt for the joke request
        prompt = f"Tell me a funny joke about {selected_topic} in a complete sentence."
        
        # Request the joke using the GenAI model
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=f"{prompt} | The rules are: 1. The joke should be funny, 2. The joke should not contain dark humor, 3. The joke should not be offensive, 4. The joke should not contain NSFW content"
        )
        
        # Log the raw response for debugging
        logging.debug(f"Raw response from GenAI: {response.text}")
        
        # Check if the response contains valid text and split into multiple jokes if any
        if response and response.text:
            jokes = response.text.strip().split('\n')  # Split by new lines if multiple jokes are returned
            unique_jokes = list(set(jokes))  # Remove duplicates by converting to a set
            logging.info(f"Unique jokes generated: {unique_jokes}")
            return random.choice(unique_jokes).strip() if unique_jokes else "No joke found."
        else:
            raise ValueError("No valid joke returned from GenAI.")
        
    except Exception as e:
        logging.error(f"Error generating joke: {e}")
        raise  # Raise the error so it can be handled in the fetch_joke function

if __name__ == "__main__":
    # Ensure Flask is running in debug mode for better error visibility
    logging.info("Starting Flask application...")
    app.run(debug=True)
