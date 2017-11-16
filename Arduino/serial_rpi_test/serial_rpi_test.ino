String dataString = "";
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
  delay(500);
  }
}
