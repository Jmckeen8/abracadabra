using UnityEditor.Scripting.Python;
using UnityEditor;
using UnityEngine;

public class MyScript : MonoBehaviour
{
    void Start()
    {
        PythonRunner.RunFile($"{Application.dataPath}/Speech Recognition/sr.py");
    }

    void Update()
    {
        
    }
}
