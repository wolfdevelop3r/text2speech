import time
import pyttsx3
import threading
import PySimpleGUI as sg

class TextToSpeech:
    def __init__(self):
        self.english_ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.greek_ascii_letters = "αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
        self.engine = pyttsx3.init()

        self.layout = [[sg.Text('Your typed characters appear here:')], [sg.Input(key='-IN-')], [sg.Button('Send'), sg.Button('Exit')], [sg.Button('Yes', size=(18, 1)), sg.Button('No', size=(19, 1))]]
        self.window = sg.Window("Text to Speech", self.layout, margins=(100, 50))

        self.run()

    def language_check(self, message):
        for i in message:
            if i in self.greek_ascii_letters:
                self.engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_elGR_Stefanos")
            elif i in self.english_ascii_letters:
                self.engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
            else:
                pass

    def say(self, message):
        while True:
            try:
                self.language_check(message)
                self.engine.say(message)
                self.engine.runAndWait()
                break
            except:
                time.sleep(0.5)

    def run(self):
        while True:
            event, values = self.window.read()

            if event == "Yes":
                threading.Thread(target=self.say, args = ("Yes",), daemon=True).start()

            if event == "No":
                threading.Thread(target=self.say, args = ("No",), daemon=True).start()

            if event == "Send":
                threading.Thread(target=self.say, args = (values['-IN-'],), daemon=True).start()

            if event == sg.WIN_CLOSED or event == "Exit":
                break

        self.window.close()

TextToSpeech()