// C++ code
//
void setup()
{
  pinMode(A5, INPUT);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(7, INPUT);
}

int buttonState = 0;
int ligaDesliga = 0;

void loop()
{
  buttonState = digitalRead(7); // Ler o estado do botão
  
  if (buttonState == 1) {
    ligaDesliga = 1;
  } else {
    ligaDesliga = 0;
  }
  
  if (ligaDesliga == 1) {
    digitalWrite(2, HIGH);
  	digitalWrite(3, HIGH);
  	digitalWrite(4, HIGH);
  }
  
  if (ligaDesliga == 0) {
  	delay(1000); // Wait for 1000 millisecond(s)
  	digitalWrite(2, LOW);
  	digitalWrite(3, LOW);
  	digitalWrite(4, LOW);
  }
}