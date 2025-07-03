#include <iostream> //input output lib
 
int main() { //execution of the program begins from int main()
  
  std::cout << "hello world\n"; //cout = character output
  
  std::string username;
  std::cout << "Enter your name: ";
  std::cin >> username; //char input (var must be declared)
  std::cout << "Hello Master " << username << "!"; //chaining

  return 0;
}

//variable types
std::string name = "kushcoded"; //part of standard lib
int level = 1;
double pi = 3.14; //float
bool cpp = true;
char grade  = 'A'; //single char, uses 'single quote'
