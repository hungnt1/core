#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <DNSServer.h>
#include <ESP8266WebServer.h>
#include <WiFiManager.h>
#include <ESP8266mDNS.h>


   
void nhandulieu (char * tp, byte * nd, unsigned int length) // tạo hàm nhận dữ liệu
  {
    String topic(tp); 
    String noidung= String((char *)nd);
    noidung.remove(length);
   Serial.println(topic);
   Serial.println(noidung);
 
     if(topic=="quạt")
    {      
        if(noidung=="bật")
         digitalWrite(5,LOW);
         if(noidung=="tắt")
         digitalWrite(5,HIGH);
    }
      if(topic=="đèn")
    {      
     if(noidung=="bật")
         digitalWrite(16,LOW);
         if(noidung=="tắt")
         digitalWrite(16,HIGH); 
    }


  
  }

  
WiFiClient c; 

PubSubClient MQTT("homeauto.local", 1883, nhandulieu, c);

void setup() 
  {
  

    Serial.begin(115200);


            

  WiFiManager wifiManager;
  wifiManager.autoConnect("Home auto switch");
        delay(500);
 while (1)
      {
        delay(500);
        if(MQTT.connect("nodemcu"))
          break;
      }
    
    Serial.println("da ket noi MQTT");  
    MQTT.subscribe("đèn"); MQTT.subscribe("hello");
    pinMode(5, OUTPUT);
    digitalWrite(5, HIGH);
    pinMode(16, OUTPUT);
    digitalWrite(16, HIGH);
    pinMode(0, INPUT);
 }
void loop() 
  {  
    if (digitalRead(0) == 0) 
    {
    WiFi.disconnect();
    delay(3000);
    setup();
     }
    if (!MQTT.connect("ESP"))
    {MQTT.connect("ESP");}
 
   MQTT.loop();
  // put your setup code here, to run once:

}


