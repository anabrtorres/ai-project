import os
import json

from model.gpt.gpt import gpt3_generate_text

path_to_dataset_json = "model/dataset.json"

dataset = {}

with open(os.path.join(os.getcwd(), path_to_dataset_json), "r") as file:
    dataset = json.load(file)


def create_answer(question):
    generate_answer = json.loads(gpt3_generate_text(question))

    print("generate: ", generate_answer)

    newAnswer = False

    for key in generate_answer:
        if generate_answer.get(key):
            for prompt in generate_answer[key]["prompt"]:
                if prompt not in dataset[key]["prompt"]:
                    newAnswer = True
                    dataset[key]["prompt"].append(prompt)

                    if generate_answer[key].get("responses"):
                        dataset[key]["responses"].append(
                            generate_answer[key]["responses"][0]
                        )

            if question not in dataset[key]["prompt"]:
                newAnswer = True
                dataset[key]["prompt"].append(question)

                if generate_answer[key].get("responses"):
                    dataset[key]["responses"].append(
                        generate_answer[key]["responses"][0]
                    )

    with open(os.path.join(os.getcwd(), path_to_dataset_json), "w") as file:
        json.dump(dataset, file, indent=4)

    if newAnswer:
        return generate_answer[key]["prompt"][0]

    return None
