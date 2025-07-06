#include <iostream>

int main() {
  double power;
  
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
  
  return 0;
} 