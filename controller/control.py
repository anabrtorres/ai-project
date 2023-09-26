import numpy as np
from PIL import Image, ImageOps
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
                        phraseIndex = dataset[key]["prompt"].index(phrase)
                        self.say(dataset[key]["responses"][phraseIndex])

                    if "recognize" in dataset[key]["actions"]:
                        result = self.recognize_imagem()
                        if result[0]:
                            self.say(f"isto é {result[1]}")
                        else:
                            self.say(dataset["unrecognizable"]["responses"][0])

                    if "stop" in dataset[key]["actions"]:
                        self.stop()

            if not hasPhrase:
                response = create_answer(phrase)
                print("created response: ", response)
                if response:
                    self.recognize_audio(response)
                else:
                    self.say(dataset["error"]["responses"][0])

    def say(self, phrase):
        print(phrase)
        self.audio.text_to_speech(phrase)

    def recognize_imagem(self):
        frame = self.vision.read_frame()
        self.vision.save_image(frame)

        # Make the image a numpy array and reshape it to the models input shape.
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # Replace this with the path to your image
        image = Image.open("imagem_captured.jpg").convert("RGB")

        # resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

        # turn the image into a numpy array
        image_array = np.asarray(image)

        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

        # Load the image into the array
        data[0] = normalized_image_array

        # Predicts the model
        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        # Print prediction and confidence score
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

        # Accept the prediction if it is greathen than 50%
        if confidence_score > 0.5:
            return [True, class_name[2:]]

        return [False]

    def stop(self):
        self.close_program = True
        self.vision.stop_capture_video()
        self.audio.stop_listening()
