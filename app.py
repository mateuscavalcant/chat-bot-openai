from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.environ["CHAT_OPENAI_KEY"]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_message = request.form['message']
    prompt = f"User: {user_message}\nChatbot: "
    chat_history = []
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\nUser: ", "\nChatbot: "]
    )

    bot_response = response.choices[0].text.strip()

    chat_history.append(f"User: {user_message} \nChatbot: {bot_response}")

    return render_template(
        "chatbot.html",
        user_message=user_message,
        bot_response=bot_response,
    )

if __name__ == '__main__':
    app.run(debug=True)
