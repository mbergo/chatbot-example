from flask import Flask, render_template, request
from chatbot import Chatbot
from chroma_db import ChromaDB

app = Flask(__name__)
chatbot = Chatbot()
chroma_db = ChromaDB('/tmp/data')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        chroma_db.index_url(url)
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.form.get('message')
    response = chatbot.respond(message)
    return response

if __name__ == '__main__':
    app.run(debug=True)
