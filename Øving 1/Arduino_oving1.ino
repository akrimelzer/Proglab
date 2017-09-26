const int buttonPin = 2; 
const int blueLed = 3; 
const int yellowLed = 4; 


// Konstanter for signaler som skal sendes 
const int dot = 0; 
const int dash = 1; 
const int letterPauseSignal = 2; 
const int wordPauseSignal = 3; 

// Konstanter tid

const float T = 300; 
const float dotTime = T;
const float dashTime = 2*T; 
const float letterPause = 7*T;
const float wordPause = 20*T; 

int buttonState;
int previousButtonState = HIGH; 

long timeFromPush; 
long releaseTime = 0; 


void setup() {
  Serial.begin(9600); 
  pinMode(buttonPin, INPUT); 
  pinMode(blueLed, OUTPUT); 
  pinMode(yellowLed, OUTPUT); 

}

void loop() {
  buttonState = digitalRead(buttonPin); 
  
  if ((buttonState == LOW) && (previousButtonState == HIGH)){
    timeFromPush = millis(); 
    previousButtonState = LOW; 
    long pause = timeFromPush - releaseTime;

    if (releaseTime != 0){
      if (pause < wordPause && pause > letterPause){
        Serial.print(letterPauseSignal);
      } else if (pause > wordPause){
        Serial.print(wordPauseSignal);
      }
    }

// Button is pushed 

  } else if ((previousButtonState == LOW && buttonState == HIGH)){
    
    previousButtonState = HIGH; 
    releaseTime = millis(); 

    long holdTime = millis() - timeFromPush; 

    if (holdTime < dashTime){
      Serial.print(dot);
      digitalWrite(yellowLed, HIGH); 
      digitalWrite(blueLed, LOW);
    } else if (holdTime > dashTime){
      Serial.print(dash);
      digitalWrite(yellowLed, LOW); 
      digitalWrite(blueLed, HIGH);
    }
    
  }
  
  delay(20); 

}
