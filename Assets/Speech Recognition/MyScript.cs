using UnityEditor.Scripting.Python;
using UnityEditor;
using UnityEngine;
using System.Threading;


public class MyScript : MonoBehaviour
{
    Thread srThread;
    
    void Start()
    {
        srThread = new Thread(runScript);
        srThread.Start();
    }

    void runScript(){
        PythonRunner.RunFile($"{Application.dataPath}/Speech Recognition/script.py");
    }
}
