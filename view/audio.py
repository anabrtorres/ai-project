import speech_recognition as sr
from gtts import gTTS
import os

class Audio:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def speech_to_text(self):
        with self.microphone as source:
            print(sr.Microphone.list_microphone_names())
            print("Fale algo...")
            self.recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
            audio = self.recognizer.listen(source)

            try:
              # Recognize the speech using Google Web Speech API
              text = self.recognizer.recognize_google(audio, language='pt-BR')
              arrText = text.split(' ')
              return text
            except sr.UnknownValueError:
              print("Sorry, I couldn't understand the audio.")
            except sr.RequestError as e:
              print("Sorry, an error occurred. Could not request results; {0}".format(e))
  
    def text_to_speech(self, phrase):
      tts = gTTS(text=phrase, lang='pt-br')
      tts.save("resposta.mp3")
      os.system("mpg321 resposta.mp3")