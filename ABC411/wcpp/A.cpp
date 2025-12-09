#include <iostream>
#include <string>

int main()
{
    std::string P;
    int L;
    std::cin >> P >> L;
    std::cout << (P.length() >= L?"Yes":"No");
    return 0;
}