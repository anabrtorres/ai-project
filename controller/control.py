import numpy as np

from controller.utils import get_random_indice_from_array
from view.audio import Audio
from view.vision import Vision
from model.dataset import dataset, create_answer
from model.ia.ia import model, class_names


class Robot:
    """
    Define a robot
    """

    def __init__(self):
        self.vision = Vision()
        self.audio = Audio()

        self.close_program = False

    def run(self):
        self.vision.start_capture_video()
        self.audio.start_listening(self.recognize_audio)

    def recognize_audio(self, phrase):
        if phrase is not None:
            phrase = phrase.lower()
            hasPhrase = False
            for key in dataset:
                if phrase in dataset[key]["prompt"]:
                    hasPhrase = True
                    if "say" in dataset[key]["actions"]:
                        if key != "other":
                            self.say(
                                dataset[key]["responses"][
                                    get_random_indice_from_array(
                                        dataset[key]["responses"]
                                    )
                                ]
                            )
                        else:
                            phraseIndex = dataset[key]["prompt"].index(phrase)
                            self.say(dataset[key]["responses"][phraseIndex])

                    if "recognize" in dataset[key]["actions"]:
                        result = self.recognize_imagem()
                        self.say(f"isto é {result}")

                    if "stop" in dataset[key]["actions"]:
                        self.stop()

            if not hasPhrase:
                print("create", phrase)
                create_answer(phrase)
                self.recognize_audio(phrase)

    def say(self, phrase):
        print(phrase)
        self.audio.text_to_speech(phrase)

    def recognize_imagem(self):
        frame = self.vision.read_frame()
        self.vision.save_image(frame)

        # Make the image a numpy array and reshape it to the models input shape.
        frame = np.asarray(frame, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array

        frame = (frame / 127.5) - 1

        # Predicts the model
        prediction = model.predict(frame)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        # Print prediction and confidence score
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

        if confidence_score > 0.5:
            return class_name[2:]

        return "Nao foi possivel reconhecer o produto"

    def stop(self):
        self.close_program = True
        self.vision.stop_capture_video()
        self.audio.stop_listening()
