# AI Chatbot Application

## Overview

This is an AI chatbot application built with FastAPI, Jinja2 and OpenAI's GPT-3.5 model. The chatbot allows users to interact with an AI-powered assistant, which can respond to user inputs with natural language responses generated by the GPT-3.5 model. Additionally, the application includes image generation features using OpenAI's DALL-E model, allowing users to generate images based on textual descriptions.

## Features

- Interactive chat interface for users to communicate with the AI assistant.
- Seamless integration with OpenAI's GPT-3.5-turbo model for generating natural language responses.
- Image generation capabilities using OpenAI's DALL-E model, allowing users to generate images based on textual descriptions.
- Web-based interface using FastAPI and Jinja2 templates.
- Support for handling concurrent chat sessions and maintaining chat history.
- Chatbot personality feature to provide a consistent tone and style in responses.

## Setup

### Prerequisites

- Python 3.11.5 installed on your system.
- OpenAI API key. You need to sign up for OpenAI and obtain an API key to use the GPT-3.5 and DALL-E models.
- Clone or download this repository to your local machine.

### Installation

1. Navigate to the root directory of the project.
2. Install dependencies using pip:

    ```
    pip install -r requirements.txt
    ```

### Configuration

1. Create a `secrets.json` file in the root directory outside the project directory (ai_chatbot).
2. Add your OpenAI API key to the `secrets.json` file:

    ```json
    {
        "OPENAI_PROJECT_KEY": "YOUR_OPENAI_API_KEY"
    }
    ```

### Running the Application

1. Open a terminal and navigate to the root directory outside the project directory (ai_chatbot).
2. Start the FastAPI server by running:

    ```
    uvicorn ai_chatbot.main:app --reload
    ```

3. Open a web browser and navigate to `http://localhost:8000/` to access the chat interface.

## Usage

- Enter your message in the text input field and press Enter or click the Send button to send it to the chatbot.
- The chatbot will respond with a natural language response generated by the GPT-3.5 model.
- You can continue the conversation by entering additional messages.
- To generate images, describe the image you want in text format, and the DALL-E model will generate an image based on the description.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please submit a pull request or open an issue on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).
