using UnityEditor.Scripting.Python;
using UnityEditor;
using UnityEngine;

public class MyScript : MonoBehaviour
{
    void Start()
    {
        PythonRunner.RunFile($"{Application.dataPath}/Scripts/script.py");
    }

    void Update()
    {
        
    }
}
