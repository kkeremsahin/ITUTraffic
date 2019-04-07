/*
 * 
 * YOUR DEFINES HERE
 * 
 * 
 * 
 */


// FILL ALL COMMENTED FUNCTIONS

#define ARDUINO_OK 10
#define RASPBERRY_OK 11

#define READ_SIGN 19

void setup(){
  
  Serial.begin(9600);
  initialize();
  
}



void loop(){


  if(Serial.available())
   switch(char a = Serial.read()){

        // MOVEMENT

    case 'L':
     //turn_left()
     break;

    case 'R':
     //turn_right();
     break;

    case 'F':
     //line_follow();
     break;


       // PARKING

    case '1':
     //to_A1();
     break;

    case '2':
     //to_A2();
     break;

    case '3':
     //to_A3();
     break;

    case '4':
     //to_B1();
     break;

    case '5':
     //to_B2();
     break;

    case '6':
     //to_B3();
     break;
     
  }


  //line_follow();

  //if(qtrDataInverted())   // uncomment this in order to detect color inversion 
     readSign();

  

}

void initialize(){

  delay(1000);
  Serial.write(ARDUINO_OK);

  while(Serial.read() != 'r');

  Serial.println("read!");

  flushIncoming();
  Serial.flush();
  
  
}
void flushIncoming(){
  while(Serial.available())
  Serial.read();
}

void readSign(){ 
    //send read signal , then halt
  
    //after halt duration data will be read in switch()
 
 Serial.write(READ_SIGN);

 //halt();          
 
 delay (1000);      // for debugging purposes only !
 
 

}

    
