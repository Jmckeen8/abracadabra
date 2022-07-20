using UnityEngine;
using System.Net;
using System.Net.Sockets;
using System.Text;


public class ProjectileColorManager : MonoBehaviour
{
    public string color; 
    public string connectionIP = "127.0.0.1";
    public int connectionPort = 25001;
    IPAddress localAdd;
    TcpListener listener;
    TcpClient client;

    void Start()
    {
        color = "Blue";
        UnityEngine.Debug.Log("Original: "+this.color);
        GetInfo();
    }

    void Update(){
        SendAndReceiveData();
    }

    void setColor(){
        ColorSingleton.Instance.setColor(color);
        UnityEngine.Debug.Log(color);
    }

    void GetInfo()
    {
        localAdd = IPAddress.Parse(connectionIP);
        listener = new TcpListener(IPAddress.Any, connectionPort);
        listener.Start();

        client = listener.AcceptTcpClient();
    }

    void SendAndReceiveData()
    {
        NetworkStream nwStream = client.GetStream();
        byte[] buffer = new byte[client.ReceiveBufferSize];

        //---receiving Data from the Host----
        int bytesRead = nwStream.Read(buffer, 0, client.ReceiveBufferSize); //Getting data in Bytes from Python
        string dataReceived = Encoding.UTF8.GetString(buffer, 0, bytesRead); //Converting byte data to string

        if (dataReceived != null)
        {
            //---Using received data---
            color = dataReceived;
            UnityEngine.Debug.Log(color);
            setColor();
        }
    }
}