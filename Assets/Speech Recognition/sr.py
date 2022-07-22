import re
import speech_recognition as sr
import time
import json
#import UnityEngine as ue



def talkToMe(audio):
    print(audio)
    for line in audio.splitlines():
        print("say " + line)

GOOGLE_CLOUD_SPEECH_CREDENTIALS = {
  ###########
}


def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        r.dynamic_energy_threshold = True
        audio = r.listen(source)

    try:
        start_time = time.time()
        command = r.recognize_google(audio).lower()
        #command = r.recognize_wit(audio, key="##########").lower()
        #command = r.recognize_azure(audio, key="##############").lower() # requires modification to SR __init__.py
        #command = r.recognize_houndify(audio, client_id="##########", client_key="########33").lower()
        #command = r.recognize_google_cloud(audio, credentials_json=json.dumps(GOOGLE_CLOUD_SPEECH_CREDENTIALS))
        elapsed_time = time.time() - start_time
        print('You said: ' + str(command))
        print("time: " + str(elapsed_time))

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

validCommands = ["blue", "red", "green"]   # can be changed to accept more words

if __name__ == "__main__":
    # while assistant(myCommand()):
    #    continue
    while True:
        command = myCommand()
        commands = command.split()
        #print(commands)
        for word in commands:
            if word in validCommands:
                print(word)
