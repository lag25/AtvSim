using UnityEngine;
using System.Net;
using System.Net.Sockets;
using System;

public class GyroDataReceiver : MonoBehaviour
{
    public int listenPort = 12345; // Port number to receive data from Python
    UdpClient udpClient;
    Animator animator;
    private void Start()
    {
        udpClient = new UdpClient(listenPort);
        animator = GetComponent<Animator>();
    }

    private void Update()
    {
        IPEndPoint remoteIpEndPoint = new IPEndPoint(IPAddress.Parse("127.0.0.1"), listenPort);
        byte[] receivedBytes = udpClient.Receive(ref remoteIpEndPoint);

        if (receivedBytes.Length == sizeof(float) * 3)
        {
            float[] gyroValues = new float[3];
            Buffer.BlockCopy(receivedBytes, 0, gyroValues, 0, receivedBytes.Length);

            float yaw = gyroValues[0];
            float pitch = gyroValues[1];
            float roll = gyroValues[2];

            // Apply gyro data to the object's rotation here
            transform.rotation = Quaternion.Euler(pitch, yaw, roll); // Apply the rotation

            // You can also adjust other parts of your animation or logic based on the gyro data
            // For example: animator.SetFloat("Yaw", yaw);
            animator.SetFloat("Yaw", yaw);
            animator.SetFloat("Pitch", pitch);
            animator.SetFloat("Roll", roll);
        }
    }

    private void OnDestroy()
    {
        udpClient.Close();
    }
}