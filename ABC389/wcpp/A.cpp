#include <iostream>
#include <string>

int main()
{
    std::string S;
    std::cin >> S;
    int a = S[0]-48, b = S[2]-48;
    std::cout << a*b;
    return 0;
}