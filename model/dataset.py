import os
import json

from model.gpt.gpt import gpt3_generate_text

path_to_dataset_json = "model/dataset.json"

dataset = {}

with open(os.path.join(os.getcwd(), path_to_dataset_json), "r") as file:
    dataset = json.load(file)


def create_answer(question):
    generate_answer = json.loads(gpt3_generate_text(question))
    print(generate_answer)

    for key in generate_answer:
        if generate_answer[key]["prompt"][0] not in dataset[key]["prompt"]:
            dataset[key]["prompt"].append(generate_answer[key]["prompt"][0])
            dataset[key]["responses"].append(generate_answer[key]["responses"][0])

    with open(os.path.join(os.getcwd(), path_to_dataset_json), "w") as file:
        json.dump(dataset, file, indent=4)
