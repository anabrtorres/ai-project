import os
import json


with open(
    os.path.join(os.getcwd(), "model/dataset.json"), "r", encoding="utf-8"
) as file:
    dataset = json.load(file)

print(dataset)
