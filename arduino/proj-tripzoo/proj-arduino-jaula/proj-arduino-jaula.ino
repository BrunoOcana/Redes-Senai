#include <SPI.h> // módulo de rede
#include <UIPEthernet.h> // módulo de rede
#include <PubSubClient.h> // mqtt
#include <Servo.h>

// Variáveis
long duracao;
float dist;
int portaoAberto;
int angulo;
Servo s;

// Configurações do Ethernet
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xAA };  // Endereço MAC do Arduino
IPAddress ip(172, 16, 32, 120);                      // Endereço IP do Arduino
IPAddress server(172, 16, 32, 206);                   // Endereço IP do servidor MQTT

EthernetClient ethClient;
PubSubClient client(ethClient);

// Configurações do MQTT
const char* portao = "mesa3-portao";  // Tópico MQTT para envio dos dados
const char* distancia = "mesa3-distancia";  // Tópico MQTT para envio dos dados
const char* clientID = "arduino-jaula";   // ID do cliente MQTT

// Pinos
const int portaoLed = 0;
const int distLed = 1;
const int portaoPin = 2;
const int trigPin = 3;
const int echoPin = 4;
const int buzzerPin = 5;
const int botaoPin = 7;

void setup() {
  Ethernet.begin(mac, ip);
  delay(1500);  // Aguarda a conexão Ethernet

  client.setServer(server, 1883);

  Serial.begin(9600);
  s.attach(8);

  pinMode(buzzerPin, OUTPUT);
  pinMode(portaoLed, OUTPUT);
  pinMode(distLed, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(portaoPin, INPUT);
  pinMode(botaoPin, INPUT_PULLUP);
}

long centimetros(long microsegundos)
{
  return microsegundos / 29 / 2;
}

void loop() {
  
  // Conectando ao servidor MQTT
  if (!client.connected()) {
    reconnect();
  }

  client.loop();
  
  // Limpa o sinal para melhor detecção
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Coloca o sensor para disparar ondas por 10 microsegundos
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duracao = pulseIn(echoPin, HIGH);
  dist = centimetros(duracao);
  
  // Alerta de proximidade
  if (distancia > 10) {
    digitalWrite(distLed, LOW);
    noTone(buzzerPin);
  }
  
  if (dist < 10 && distancia > 5) {
    digitalWrite(distLed, LOW);
    tone(buzzerPin, 400, 100);
    delay(50);
    noTone(buzzerPin);
  }
  
  if (dist <= 5) {
    digitalWrite(distLed, HIGH);
    tone(buzzerPin, 1000, 100);
    delay(100);
    noTone(buzzerPin);
    digitalWrite(distLed, LOW);
    tone(buzzerPin, 1000, 100);
    delay(100);
    noTone(buzzerPin);
  }
  
  // Abrindo o portão
  if(digitalRead(botaoPin) == LOW){
    portaoAberto = 1;
    for( angulo = 0; angulo <= 90; angulo ++){
      s.write(angulo);
      delay(10);
    }
    delay(5000);
    portaoAberto = 0;
    for( angulo = 90; angulo >= 0; angulo --){
      s.write(angulo);
      delay(10);
    }
  }

  // Alarme do portão aberto
  if (portaoAberto == 1) {
    digitalWrite(portaoLed, HIGH);
    tone(buzzerPin, 700, 1000);
    delay(50);
    digitalWrite(portaoLed, LOW);
    noTone(buzzerPin);
    delay(50);
    digitalWrite(portaoLed, HIGH);
    tone(buzzerPin, 700, 1000);
    delay(50);
    digitalWrite(portaoLed, LOW);
    noTone(buzzerPin);
    delay(50);
  }

  // Converter os valores para string e publicar no MQTT
  char portaoStr[4];
  dtostrf(portaoAberto, 6, 1, portaoStr);
  client.publish(portao, portaoStr);
  char distStr[4];
  dtostrf(dist, 6, 1, distStr);
  client.publish(distancia, distStr);
  delay(100);
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
