#include <iostream>

long long lcm(int a, int b) {
  //write your code here
  return a*b;
}

int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << lcm(a, b) << std::endl;
  return 0;
}
