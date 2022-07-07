import re

import speech_recognition as sr
import os


def talkToMe(audio):
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)
        print()


def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command)

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand()

    return command


def assistant(command):
    if re.search(r"quit|exit|close", command, re.IGNORECASE):
        return False
    else:
        talkToMe(f'You said {command}')
        return True


if __name__ == "__main__":
    while assistant(myCommand()):
        continue
