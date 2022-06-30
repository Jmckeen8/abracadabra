import time

import speech_recognition as sr
import os


def talkToMe(audio):
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)


def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand()

    return command


def assistant(command):
    if 'quick' or 'exit' or 'close' in command:
        return False
    else:
        talkToMe(f'You said {command}')
        return True


if __name__ == "__main__":
    while True:
        assistant(myCommand())
        time.sleep(1)
