#import UnityEngine
import speech_recognition as sr
import socket
import traceback
import threading


validCommands = ["blue", "red", "green"]   # can be changed to accept more words

commandMappings = {}

host, port = "127.0.0.1", 25001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        r.dynamic_energy_threshold = True
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        #command = r.recognize_houndify(audio, client_id="oOyrgxTOCCk0qIHCUDjWXw==", client_key="BOUmRQg8lMm74vc2sejcxxwaxC1hQpaqt5jwzJD3Tf39Zhib7g7zd4idTcXLoeTqq4fqziI5LqiY3Mks8382UQ==").lower()
        print('You said: ' + command)

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand()

    return command


def combine(term1, term2):
    if term1 == "red" or term2=="red":
        if term1 == "blue" or term2 == "blue":
            return "purple"
        elif term1 == "green" or term2 == "green":
            return "brown"
        else:
            return term1
    elif (term1 == "blue" or term2 == "blue") and (term1 == "green" or term2 == "green"):
        return "teal"

#save "x" as "y" and "x"
def execute():
    sock.sendall("Red".encode("UTF-8"))
    while True:
        command = myCommand()
        commands = command.split()
        try:
            for i, word in enumerate(commands):
                if word =="remember":
                    commandMappings[commands[i+1]] = combine(commands[i+2], commands[i+3])
                    print("saving " + str(commandMappings[commands[i+1]]) + " as " + str(commands[i+1]))
                    break
                else:
                    if commandMappings.get(word) is not None:
                        sock.sendall(commandMappings.get(word).encode("UTF-8")) #Converting string to Byte, and sending it to C#
                        print(commandMappings.get(word))
                    else:
                        sock.sendall(word.encode("UTF-8")) #Converting string to Byte, and sending it to C#
                        print(word)
        except:
            print("exception")
        # for word in commands:
        #     sock.sendall(word.encode("UTF-8")) #Converting string to Byte, and sending it to C#


try:
    threading.Thread(target=execute).start()
except:
   #UnityEngine.Debug.Log("Error: Thread not running")
   print("Error: Thread not running")
   traceback.print_exc()

