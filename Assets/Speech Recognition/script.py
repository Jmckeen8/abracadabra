import UnityEngine
import speech_recognition as sr

validCommands = ["blue", "red", "green"]   # can be changed to accept more words

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
        print('You said: ' + command)

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand()

    return command


all_objects = UnityEngine.Object.FindObjectsOfType(UnityEngine.GameObject)
for go in all_objects:
    try:
        if "Player" in go.name and not "Health" in go.name:
            UnityEngine.Debug.Log("found")
            UnityEngine.Debug.Log(go.name)
            #UnityEngine.Debug.Log(go.GetComponent<ProjectileColorManager>().color)
            #go.GetComponent("ProjectileColorManager").setColor("Red")
            while True:
                command = myCommand()
                commands = command.split()
                for word in commands:
                    if word in validCommands:
                        go.SendMessage("setColor", word)

    except Exception as e:
        UnityEngine.Debug.Log("Error")
        if hasattr(e, 'message'):
            UnityEngine.Debug.Log(e.message)
        else:
            UnityEngine.Debug.Log(e)