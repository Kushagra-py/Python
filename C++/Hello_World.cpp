#include <iostream> //input output lib


//define function
void function() {
  std::cout << "Bye World!" << std::endl;
}
 

int main() { //execution of the program begins from int main()
  
  std::cout << "Hello world!\n"; //cout = character output
  
  std::string username;
  std::cout << "Enter your name: ";
  std::cin >> username; //char input (var must be declared)
  std::cout << "Hello Master " << username << "!" << std::endl; //chaining



//variable types
std::string name = "kushcoded"; //part of standard lib
int File_number = 1;
double pi = 3.14; //float
bool cpp = true;
char grade  = 'A'; //single char, uses 'single quote'

/*
operators:
== equal to
!= not equal to
> greater than
< less than
>= greater than or equal to
<= less than or equal to

logical operators:  
&& and
|| or
! not
*/

//conditionals
  int power;
  
  std::cout << "Enter power level: ";
  std::cin >> power;
  
  if (power > 9000) {
    std::cout << "IT'S OVER 9000!" << std::endl; // \n + std::flush = std::endl
  }
  else if (power == 9000) {
    std::cout << "Almost there..." << std::endl;
  }
  else {
    std::cout << "You are weak!" << std::endl;
  }
  

//for loop
for(int i = 0; i < 10; i++) {
    std::cout << i << std::endl;
}
std::cout << "warmup complete" << std::endl;

//while loop
int countdown;
std::cout << "Countdown from: ";
std::cin >> countdown;
while(countdown != 0) {
    std::cout << countdown << std::endl;
    countdown--;
}

function(); //function call

return 0;
}