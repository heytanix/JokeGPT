from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS  # Import CORS
from google import genai
from dotenv import load_dotenv
import os
import random

# Loading the environment variables from ".env" file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize the GenAI client with the API key
api_key = os.getenv("API_KEY")  # Load API key from environment variable
client = genai.Client(api_key=api_key)

def get_joke():
    # List of topics for jokes
    topics = [
        "animals",
        "sports",
        "food",
        "technology",
        "travel",
        "music",
        "movies",
        "science",
        "history",
        "books"
    ]
    
    # Randomly select a topic
    selected_topic = random.choice(topics)
    
    # General prompt to generate a random joke
    prompt = f"Tell me a funny joke about {selected_topic} in a complete sentence."
    
    # Generation of content using the Gemini-2.0-Flash model
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=f"{prompt} | The rules are: 1. The joke should be funny, 2. The joke should not contain dark humor, 3. The joke should not be offensive, 4. The joke should not contain NSFW content"
    )
    
    # Debugging: Print the raw response
    print("Raw response from GenAI:", response.text)
    
    # Assuming the response contains the joke in a specific format
    jokes = response.text.strip().split('\n')  # Split by new lines if multiple jokes are returned
    unique_jokes = list(set(jokes))  # Remove duplicates by converting to a set
    
    # Debugging: Print the unique jokes
    print("Unique jokes generated:", unique_jokes)
    
    # Return a random unique joke, ensuring it's a single string
    return random.choice(unique_jokes).strip() if unique_jokes else "No joke found."

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')  # Serve index.html from the current directory

@app.route('/get_joke', methods=['GET'])
def fetch_joke():
    try:
        joke = get_joke()  # Get a random joke
        print("Generated joke:", joke)  # Debugging output
        return jsonify({"joke": joke})  # Return the joke as a JSON response
    except Exception as e:
        print("Error fetching joke:", str(e))  # Print the error
        return jsonify({"error": str(e)}), 500  # Return error as JSON

@app.route('/<path:filename>', methods=['GET'])
def serve_static(filename):
    return send_from_directory('.', filename)  # Serve static files (CSS, etc.)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)  # Run the Flask app in debug mode
