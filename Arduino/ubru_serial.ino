char dataString[50] = {0};


void setup() {
	Serial.begin(9600);
}

void loop() {
	a++;
	sprintf(dataString, "Nope"); 
	Serial.println(dataString);
	delay(1000);
}