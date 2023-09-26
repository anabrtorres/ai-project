import os
import json
import openai
from config_secret import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

path_to_instructions = "model/gpt/instructions.txt"
path_to_last_response = "model/gpt/last_response.json"

with open(os.path.join(os.getcwd(), path_to_instructions), "r") as arquivo:
    instructions = arquivo.read()


def gpt3_generate_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": prompt},
        ],
    )

    content = response["choices"][0]["message"]["content"]

    with open(os.path.join(os.getcwd(), path_to_last_response), "w") as file:
        json.dump(content, file, indent=4)

    return content


# print(gpt3_generate_text("Ola"))
