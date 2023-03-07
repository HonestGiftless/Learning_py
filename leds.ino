#define ledPin1 6
#define ledPin2 7

int ledState1 = LOW;
unsigned long previousMillis1 = 0;

int ledState2 = LOW;
unsigned long previousMillis2 = 0;


void setup() 
{
  pinMode(ledPin1, OUTPUT);      
  pinMode(ledPin2, OUTPUT);      
}

void loop()
{
  unsigned long currentMillis = millis();
 
  if((ledState1 == HIGH) && (currentMillis - previousMillis1 >= 450))
  {
    ledState1 = LOW;
    previousMillis1 = currentMillis;
    digitalWrite(ledPin1, ledState1);
  }
  else if ((ledState1 == LOW) && (currentMillis - previousMillis1 >= 150))
  {
    ledState1 = HIGH;
    previousMillis1 = currentMillis;
    digitalWrite(ledPin1, ledState1);
  }
  
  if((ledState2 == HIGH) && (currentMillis - previousMillis2 >= 250))
  {
    ledState2 = LOW;
    previousMillis2 = currentMillis;
    digitalWrite(ledPin2, ledState2);
  }
  else if ((ledState2 == LOW) && (currentMillis - previousMillis2 >= 250))
  {
    ledState2 = HIGH;
    previousMillis2 = currentMillis;
    digitalWrite(ledPin2, ledState2);
  }
}
