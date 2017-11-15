//char dataString[50] = {0};
String dataString = "";
char stringOne[5] = "One!";
char stringTwo[5] = "Two!";
int indOne = 0;
int indTwo = 0;
int state;
//int incomingByte = 0;
void setup() {
  // put your setup code here, to run once:
  state = 0;
  Serial.begin(9600);
}

void loop() {
  
  // send data only when you receive data:
  if (Serial.available() > 0) {
    
    // read the incoming byte:
    dataString = Serial.readString();
    delay(300);
    if(dataString == "1") {
      Serial.println("One!");
    } else if (dataString == "2") {
      Serial.println("Two!");
    } else {
      Serial.println("No!");
    }
    /*if(state == 0) {
      while(Serial.available() <= 0) {
        // Initalize state
        if(dataString == "1") {
          state = 1;
        } else if (dataString == "2") {
          state = 2;
        }
        Serial.println("r");
      }
    }
    else if(state) {
      // Done with message, clear variables
      if(dataString == "d") {
        state = 0;
        dataString = "";
      }
      // Sending message
      else {
        // Ready for next byte
        if(state == 1) {
          Serial.println("One!");
        } else if(state == 2) {
          Serial.println("Two!");
        }
      }
    }*/
  /*} else {
    Serial.println("Noo!");
    } */
  delay(500);
  }
}
