import os
import threading
import speech_recognition as sr
from gtts import gTTS


class Audio:
    """
    Class represents the robot's audio recognition methods.
    Listen and speak.
    """

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        self.thread_audio = None

        self.close_program = False

    def start_listening(self, callback):
        print(callback)
        self.thread_audio = threading.Thread(target=self._listening, args=(callback,))
        self.thread_audio.start()

    def stop_listening(self):
        self.close_program = True
        self.thread_audio.join()

    def _listening(self, callback):
        while not self.close_program:
            stt = self.speech_to_text()
            # stt = input("Text: ")
            print(stt, self.close_program)

            callback(stt)

    def speech_to_text(self):
        with self.microphone as source:
            print(sr.Microphone.list_microphone_names())
            print("Fale algo...")
            self.recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
            audio = self.recognizer.listen(source)

            try:
                # Recognize the speech using Google Web Speech API
                text = self.recognizer.recognize_google(audio, language="pt-BR")
                return text
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand the audio.")
            except sr.RequestError as err:
                print(f"Sorry, an error occurred. Could not request results; {err}")

    def text_to_speech(self, phrase):
        tts = gTTS(text=phrase, lang="pt-br")
        tts.save("resposta.mp3")
        os.system("mpg321 resposta.mp3")
