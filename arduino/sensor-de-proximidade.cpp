

long duracao;
int distancia;

// Pinos de conexão
const int trigPin = 11;
const int echoPin = 10;
const int ledVerPin = 2;
const int ledAmPin = 4;
const int ledGrPin = 7;
const int buzzerPin = 9;


void setup()
{
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(ledGrPin, OUTPUT);
  pinMode(ledAmPin, OUTPUT);
  pinMode(ledVerPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
}

long centimetros(long microsegundos)
{
  return microsegundos * 0.034 / 2;
}

void loop()
{
  // Limpa o sinal para melhor detecção
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Coloca o sensor para disparar ondas por 10 microsegundos
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duracao = pulseIn(echoPin, HIGH);
  distancia = centimetros(duracao);
  
  if (distancia > 100) {
    digitalWrite(ledGrPin, HIGH);
    digitalWrite(ledAmPin, LOW);
    digitalWrite(ledVerPin, LOW);
    noTone(buzzerPin);
  }
  
  if (distancia < 100 && distancia > 50) {
    digitalWrite(ledGrPin, LOW);
    digitalWrite(ledAmPin, HIGH);
    digitalWrite(ledVerPin, LOW);
    tone(buzzerPin, 400, 1000);
    delay(500);
  }
  
  if (distancia <= 50) {
    digitalWrite(ledGrPin, LOW);
    digitalWrite(ledAmPin, LOW);
    digitalWrite(ledVerPin, HIGH);
    tone(buzzerPin, 1000, 1000);
    delay(200);
  }
}
