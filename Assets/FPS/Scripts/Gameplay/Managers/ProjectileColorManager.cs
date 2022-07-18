using UnityEngine;

public class ProjectileColorManager : MonoBehaviour
{
    public string color; 

    void Start()
    {
        color = "Blue";
        UnityEngine.Debug.Log("Original: "+this.color);
    }

    void setColor(string newColor){
        this.color = newColor;
        ColorSingleton.Instance.setColor(color);
        UnityEngine.Debug.Log(this.color);
    }
}
