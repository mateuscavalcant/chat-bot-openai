# chat-bot-openai

Developing a Chatbot with OpenAI API and Python Flask.

## Description

This project is a application built with Python using the Flask web framework and powered by the OpenAI API.
Users can enter messages in the input field and receive responses from the chatbot based on the model's generated text.
The chatbot uses the `text-davinci-003` model provided by OpenAI.

## Installation

To run the Chatbot Project locally, follow these steps:

1. Clone the repository.

2. Navigate to the project directory:
```sh
cd chat-bot-openai
```

3. Install the required dependencies:
```sh
pip install flask
```
```sh
pip install openai
```
```sh
pip install python-dotenv
```
4. Set up your OpenAI API credentials:
- Add your OpenAI API key to the `.env` file.

5. Run the application:
- Run the Flask application using ` python app.py ` in your terminal.


6. Access the chatbot in your web browser at `http://localhost:5000`.

## Usage

Once the application is running, you can interact with the chatbot through the provided chat interface. Enter your message in the input field and press "Send" to receive the chatbot's response.





