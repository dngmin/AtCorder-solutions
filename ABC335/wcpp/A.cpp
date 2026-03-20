#include <iostream>
#include <string>

int main()
{
    std::string S;
    std::cin >> S;
    std::cout << S.substr(0,S.size()-1) << 4 << std::endl;
    return 0;
}