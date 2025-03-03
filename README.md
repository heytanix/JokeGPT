# JokeGPT

## Deployed Link

[View the live application here](<https://joke-gpt-five.vercel.app/>)

## Overview

JokeGPT is a web application that generates and serves jokes using the power of the Gemini 2.0 Flash AI model. The application is built with Flask, a lightweight WSGI web application framework in Python, and utilizes the Google GenAI API to generate jokes based on various topics. The frontend is designed with HTML and CSS, providing a user-friendly interface for users to interact with the application.

## Features

- **Joke Generation**: Fetches random jokes based on selected topics such as animals, sports, food, technology, and more. The jokes are generated using advanced AI algorithms to ensure they are funny and appropriate.
- **CORS Support**: The application supports Cross-Origin Resource Sharing (CORS) to allow requests from different origins, making it easier to integrate with other web applications.
- **Responsive Design**: The frontend is designed to be responsive and user-friendly, ensuring a good experience on both desktop and mobile devices. The layout adjusts seamlessly to different screen sizes.
- **Error Handling**: Comprehensive error handling is implemented to manage issues during joke fetching and generation, providing users with informative feedback in case of errors.

## Technologies Used

- **Backend**: 
  - **Python**: The primary programming language used for backend development.
  - **Flask**: A lightweight WSGI web application framework for Python, used to create the web server and handle requests.
  - **Flask-CORS**: A Flask extension that allows cross-origin requests, enabling the frontend to communicate with the backend.
  - **Google GenAI API**: Utilized for generating jokes based on various topics using AI.
  - **dotenv**: A library for managing environment variables, ensuring sensitive information like API keys are kept secure.

- **Frontend**: 
  - **HTML**: The standard markup language used to create the structure of the web pages.
  - **CSS**: Used for styling the application, ensuring a visually appealing user interface.
  - **JavaScript**: Employed for making asynchronous requests to the backend to fetch jokes without reloading the page.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.x**: The programming language required to run the application.
- **pip**: The Python package installer, used to install the required packages.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/heytanix/JokeGPT.git
   cd JokeGPT
   ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment variables**:
   - Create a `.env` file in the root directory of the project.
   - Add your API key:
     ```
     API_KEY=your_google_genai_api_key (confidential - Present in ".env" file)
     ```

### Running the Application

To run the application, execute the following command in your terminal:

```bash
python JokeGPT.py
```

Once the application is running, you can access it in your web browser at `http://localhost:5000`.

### Usage

- Click the "Get a Joke" button on the homepage to fetch a random joke. The joke will be displayed on the screen, and the background and text colors will toggle between black and white for better visibility.

### Troubleshooting

- If you encounter issues with fetching jokes, ensure that your API key is correctly set in the `.env` file and that you have an active internet connection.
- Check the console for any error messages that may provide insight into what went wrong.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the developers of Flask and the Google GenAI API for providing the tools that made this project possible.
- Special thanks to the open-source community for their contributions and support.
