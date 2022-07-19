using UnityEditor.Scripting.Python;
using UnityEditor;
using UnityEngine;

public class MyScript : MonoBehaviour
{
    void Start()
    {
        srThread = new Thread(runScript);
        srThread.Start();
    }

    void runScript(){
        PythonRunner.RunFile($"{Application.dataPath}/Speech Recognition/script.py");
    }
}
