import openai
import langchain
from tensorflow.keras.preprocessing.text import Tokenizer

tokenizer = Tokenizer(num_words=1000)


class Chatbot:
    def __init__(self):
        self.model = 'gpt-3.5-turbo'
        self.tokenizer = langchain.Tokenizer()

    def respond(self, message):
        tokens = self.tokenizer.tokenize(message)
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": tokens},
            ]
        )
        return response.choices[0].message['content']
