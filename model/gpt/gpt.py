import os
import openai
from config_secret import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

with open(os.path.join(os.getcwd(), "model/gpt/instructions.txt"), "r") as arquivo:
    instructions = arquivo.read()


def gpt3_generate_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": prompt},
        ],
    )
    return response["choices"][0]["message"]["content"]
