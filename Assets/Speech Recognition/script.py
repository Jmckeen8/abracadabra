import UnityEngine
import sr

validCommands = ["blue", "red", "green"]   # can be changed to accept more words

all_objects = UnityEngine.Object.FindObjectsOfType(UnityEngine.GameObject)
for go in all_objects:
    try:
        if "Player" in go.name and not "Health" in go.name:
            UnityEngine.Debug.Log("found")
            UnityEngine.Debug.Log(go.name)
            #UnityEngine.Debug.Log(go.GetComponent<ProjectileColorManager>().color)
            go.GetComponent("ProjectileColorManager").setColor("Red")
            # while True:
            #     command = sr.myCommand()
            #     commands = command.split()
            #     for word in commands:
            #         if word in validCommands:
            #             go.SendMessage("setColor", word)

    except Exception as e:
        UnityEngine.Debug.Log("Error")
        if hasattr(e, 'message'):
            UnityEngine.Debug.Log(e.message)
        else:
            UnityEngine.Debug.Log(e)