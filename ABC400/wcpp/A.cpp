#include <iostream>

int main()
{
    int A, B;
    std::cin >> A;
    std::cout << (400%A == 0?400/A:-1);
    return 0;
}