

const int ledPinRed = 3;
const int ledPinAzul = 5;
const int ledPinVerde = 6;
const int tempPin = A0;
float temp;
float vout;
int vermelho;
int verde;
int azul;

void setup()
{
  pinMode(ledPinRed, OUTPUT);
  pinMode(ledPinAzul, OUTPUT);
  pinMode(ledPinVerde, OUTPUT);
  pinMode(tempPin, INPUT);
}

void loop()
{
  // Conversão de volts para temperatura Celsius
  float vout = analogRead(tempPin)*0.004882814;
  float temp = (vout - 0.5) * 100.0;
  
  // Verificando a temperatura
  if (temp > 20 ) {
    vermelho = 255;
  }
  else {
    vermelho = 0;
  }
  
  if (temp <= 30 && temp > 0 ) {
    verde = 255;
  }
  else {
    verde = 0;
  }
  
  if (temp >= -10 && temp < 10) {
    azul = 255;
  }
  else {
    azul = 0;
  }
  
  // Settando cor no led rgb
  digitalWrite(ledPinRed, vermelho);
  digitalWrite(ledPinVerde, verde);
  digitalWrite(ledPinAzul, azul);
}
