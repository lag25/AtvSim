#include <WiFi.h>
#include <WebSocketsServer.h>
#include <Wire.h>
#include "MPU9250.h"

const char* ssid = "Airel_9826216560";
const char* password = "air80318";

WebSocketsServer webSocket = WebSocketsServer(81);

MPU9250 mpu;

void setup() {
  Serial.begin(115200);
  Wire.begin();
  delay(1000);
  if (!mpu.setup(0x68)) {  
        while (1) {
            Serial.println("MPU connection failed. Please check your connection with `connection_check` example.");
            
        }
    }
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
  Serial.print("ESP32 IP Address: ");
  Serial.println(WiFi.localIP());

  webSocket.begin();
  
  
}

void loop() {
  mpu.update();
  float gyroX = mpu.getYaw();
  float gyroY = mpu.getPitch();
  float gyroZ = mpu.getRoll();
  
  String data = String(gyroX) + "," + String(gyroY) + "," + String(gyroZ);
 // Serial.println(data);
  webSocket.broadcastTXT(data);
  
  webSocket.loop();
}
