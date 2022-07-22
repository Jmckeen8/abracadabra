using UnityEngine;

public sealed class ColorSingleton
{
    private static ColorSingleton instance = null;
    private static readonly object padlock = new object();
    private static Color color;

    ColorSingleton()
    {
        color = new Color(0.0f,0.0f,1.0f,1.0f);
    }

    public static ColorSingleton Instance
    {
        get
        {
            lock (padlock)
            {
                if (instance == null)
                {
                    instance = new ColorSingleton();
                }
                return instance;
            }
        }
    }

    public void setColor(string newColor){
        if(newColor.ToLower().Contains("red")){
            color = new Color(1.0f,0.0f,0.0f,1.0f);
        } else if(newColor.ToLower().Contains("blue")){
            color = new Color(0.0f,0.0f,1.0f,1.0f);
        } else if(newColor.ToLower().Contains("green")){
            color = new Color(0.0f,1.0f,0.0f,1.0f);
        } else if(newColor.ToLower().Contains("purple")){
            color = new Color(0.6f,0.2f,1.0f,1.0f);
        } else if(newColor.ToLower().Contains("brown")){
            color = new Color(0.4f,0.2f,0.0f,1.0f);
        } else if(newColor.ToLower().Contains("teal")){
            color = new Color(0.0f,0.6f,0.6f,1.0f);
        }
    }

    public Color getColor(){
        return color;
    }
}