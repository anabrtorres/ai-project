from controller.utils import getRandomIndice
from view.audio import Audio
from view.vision import Vision
from model.dataset import dataset

import threading

class Robot:
    def __init__(self):
        self.vision = Vision()
        self.audio = Audio()

        self.close_program = False

    def run(self):
        self.vision.start_capture_video()
        self.thread_audio = threading.Thread(target=self.listening)
        self.thread_audio.start()
        self.thread_audio.join()

    def listening(self):
        while not self.close_program:
            
            # stt = self.audio.speech_to_text()
            stt = input("Text: ")
            print(stt, self.close_program)

            self.recognize(stt)

    def recognize(self, phrase):
        if phrase != None:
                phrase = phrase.lower()
                for key in dataset:
                    if phrase in dataset[key]['keys']:

                        if "say" in dataset[key]["actions"]:
                            self.say(dataset[key]["responses"][getRandomIndice(dataset[key]["responses"])])
                        
                        if "see" in dataset[key]["actions"]:
                            self.see()
                        
                        if "stop" in dataset[key]["actions"]:
                            self.stop()

    def say(self, phrase):
        print(phrase)
        self.audio.text_to_speech(phrase)
    
    def see(self):
        self.vision.save_image('imagem_captured.jpg')

    def stop(self):
        self.close_program = True
        self.vision.stop_capture_video()
