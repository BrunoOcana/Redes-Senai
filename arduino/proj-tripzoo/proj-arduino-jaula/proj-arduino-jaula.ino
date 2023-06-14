#include <SPI.h> // módulo de rede
#include <UIPEthernet.h> // módulo de rede
#include <PubSubClient.h> // mqtt
#include <Servo.h>

// Variáveis
long duracao;
float dist;
int portaoAberto;
int angulo;
int alerta;
Servo s;

// LEDs
int l1;
int l2;
int l3;

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
#define closeLed 0
#define middleLed 1
#define distLed 2
#define trigPin 3
#define echoPin 4
#define buzzerPin 5
#define potPin A0
#define servoPin 8

void setup() {
  Ethernet.begin(mac, ip);
  delay(1500);  // Aguarda a conexão Ethernet

  client.setServer(server, 1883);

  Serial.begin(9600);
  s.attach(8);

  pinMode(closeLed, OUTPUT);
  pinMode(middleLed, OUTPUT);
  pinMode(distLed, OUTPUT);
  
  pinMode(buzzerPin, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  pinMode(servoPin, INPUT);
  pinMode(potPin, INPUT);
}

long centimetros(long microsegundos) {
  return microsegundos / 29 / 2;
}

void loop() {
  
  // Conectando ao servidor MQTT
  if (!client.connected()) {
    reconnect();
  }

  client.loop();
  
  // Controlando o portão
  float controlePortao = map(analogRead(potPin), 0, 1023, 0, 90);
  // analogWrite(servoPin, controlePortao);
  
  for (angulo < 90; angulo < controlePortao; angulo ++){
    s.write(angulo);
    delay(10);
  }
  // for(int angulo = 0; angulo <= -90; angulo ++){
  // for(int angulo = -90; angulo >= 0; angulo --){
  for (angulo > 0; angulo > controlePortao; angulo --){
    s.write(angulo);
    delay(10);
  }


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
  if (distancia > 15) {
    l1 = "LOW";
    l2 = "LOW";
    l3 = "HIGH";
    alerta = 0;
    Serial.println("Alerta nível 0.");
  } else if (dist < 15 && distancia > 7) {
    l1 = "LOW";
    l2 = "HIGH";
    l3 = "HIGH";
    alerta = 1;
    Serial.println("Alerta nível 1.");
  } else if (dist <= 7) {
    l1 = "HIGH";
    l2 = "HIGH";
    l3 = "HIGH";
    alerta = 2;
    Serial.println("Alerta nível 2.");
  } else {
    l1 = "LOW";
    l2 = "LOW";
    l3 = "LOW";
    alerta = -1;
    Serial.println("Erro ao ler a proximidade.");
  }
    
  // Buzzer
  if (alerta < 1) {
    noTone(buzzerPin);
  } else if (alerta = 1) {
    tone(buzzerPin, 1000, 200);
    delay(200);
    noTone(buzzerPin);
  } else if (alerta = 2) {
    tone(buzzerPin, 1000, 100);
    delay(100);
    noTone(buzzerPin);
  }

  // LEDs
  digitalWrite(closeLed, l1);
  digitalWrite(middleLed, l2);
  digitalWrite(distLed, l3);

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
