#include <LiquidCrystal.h> // LCD
#include <DHT11.h> // sensor temp + umid
#include <SPI.h> // módulo de rede
#include <UIPEthernet.h> // módulo de rede
#include <PubSubClient.h> // mqtt

// Configurações do Ethernet
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xA9 };  // Endereço MAC do Arduino
IPAddress ip(172, 16, 32, 119);                      // Endereço IP do Arduino
IPAddress server(172, 16, 32, 206);                   // Endereço IP do servidor MQTT

EthernetClient ethClient;
PubSubClient client(ethClient);

// Configurações do MQTT
const char* luz = "mesa3-luz";  // Tópico MQTT para envio dos dados
const char* temp = "mesa3-temperatura";  // Tópico MQTT para envio dos dados
const char* umid = "mesa3-umidade";  // Tópico MQTT para envio dos dados
const char* clientID = "mesa3-arduino-data";   // ID do cliente MQTT

// Pinos do LCD
const int rs = 2, en = 1, d4 = 4, d5 = 5, d6 = 6, d7 = 7;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

// Pinos dos sensores
DHT11 dht11(A1);
const int sensLuz = A2;

void setup() {
  Ethernet.begin(mac, ip);
  delay(1500);  // Aguarda a conexão Ethernet

  pinMode(sensLuz, INPUT);

  Serial.begin(9600);
  client.setServer(server, 1883);

  // Colunas e linhas do LCD
  lcd.begin(16, 2);
  lcd.print("Mesa 03, TripZoo");
}

void loop() {
  
  // Conectando ao servidor MQTT
  if (!client.connected()) {
    reconnect();
  }

  client.loop();
  
  // Lendo os dados do clima
  float u = dht11.readHumidity();
  float t = dht11.readTemperature();
  
  // Lendo o sensor de luminosidade
  float l = analogRead(sensLuz);

  if (t >= 0 && u > 0)
    {
        Serial.print("Temperatura: ");
        Serial.print(t);
        Serial.println(" C");
        
        Serial.print("Umidade: ");
        Serial.print(u);
        Serial.println(" %");

        Serial.print("Luminosidade: ");
        Serial.print(l);
        Serial.println(" un");

        lcd.setCursor(0,0);
        lcd.print("Temp: ");
        lcd.print(t);
        lcd.print(" C");
        lcd.setCursor(0,1);
        lcd.print("Umid: ");
        lcd.print(u);
        lcd.print(" %");
        lcd.noCursor();
        delay(2000);
    }
    else
    {
        // Ao falhar a leitura, mostrar a mensagem:
        Serial.println("Erro DHT11 ou Lum");
        lcd.clear();
        lcd.setCursor(0,0);
        lcd.print("Erro!");
        lcd.setCursor(0,1);
        lcd.print("Coletar Dados");
        lcd.noCursor();
        delay(2000);
    }

  // Converter os valores para string e publicar no MQTT
  char uStr[4];
  dtostrf(u, 6, 1, uStr);
  client.publish(umid, uStr);
  char tStr[4];
  dtostrf(t, 6, 1, tStr);
  client.publish(temp, tStr);
  char lStr[4];
  dtostrf(l, 6, 1, lStr);
  client.publish(luz, lStr);

  // Esperar uma nova leitura
  delay(2000);
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Conectando ao servidor MQTT...");
    
    if (client.connect(clientID)) {
      Serial.println("conectado!");
    } else {
      Serial.print(" falhou, código do erro: ");
      Serial.print(client.state());
      Serial.println(" Tentando novamente em 5 segundos...");
      
      delay(10000);  // Aguarda 5 segundos antes de tentar a conexão novamente
    }
  }
}