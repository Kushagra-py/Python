#include <iostream>
#include <cstdlib> //Random module

int main(){
  srand(time(NULL)); // Seed the random number generator

  int dice = std::rand() % 6;  // Generates a random number that's either 0, 1, 2, 3, 4, 5

  std::cout << "You rolled a " << dice << std::endl;
  return 0;
}