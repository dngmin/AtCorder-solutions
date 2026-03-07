#include <iostream>
#include <string>

int main()
{
    std::string S;
    std::cin >> S;
    std::cout << (S == "<" + std::string(S.size()-2,'=') + ">"? "Yes":"No");
    return 0;
}