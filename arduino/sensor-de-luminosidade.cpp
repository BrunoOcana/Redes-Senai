const int ledGrPin = 7;
const int ledAmPin = 4;
const int ledVerPin = 2;
const int sensLuz = A0;

void setup()
{
  pinMode(ledGrPin, OUTPUT);
  pinMode(ledAmPin, OUTPUT);
  pinMode(ledVerPin, OUTPUT);
  pinMode(sensLuz, INPUT);
}

void loop()
{
float luz = analogRead(sensLuz)*2;
  
  if (luz < 200) {
    digitalWrite(ledGrPin, LOW);
    digitalWrite(ledAmPin, LOW);
    digitalWrite(ledVerPin, HIGH);
  } else {
    if (luz < 400) {
    digitalWrite(ledGrPin, LOW);
    digitalWrite(ledAmPin, HIGH);
    digitalWrite(ledVerPin, HIGH);
    } else {
      if (luz >= 400) {
      digitalWrite(ledGrPin, HIGH);
      digitalWrite(ledAmPin, HIGH);
      digitalWrite(ledVerPin, HIGH);
      }
    }
  }
}
