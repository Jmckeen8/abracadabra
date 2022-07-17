import UnityEngine

all_objects = UnityEngine.Object.FindObjectsOfType(UnityEngine.GameObject)
for go in all_objects:
    try:
        if "Player" in go.name and not "Health" in go.name:
            UnityEngine.Debug.Log("found")
            UnityEngine.Debug.Log(go.name)
            #UnityEngine.Debug.Log(go.GetComponent<ProjectileColorManager>().color)
            #go.GetComponent("ProjectileColorManager").setColor("Red")
            go.SendMessage("setColor","Red")
    except Exception as e:
        UnityEngine.Debug.Log("Error")
        if hasattr(e, 'message'):
            UnityEngine.Debug.Log(e.message)
        else:
            UnityEngine.Debug.Log(e)