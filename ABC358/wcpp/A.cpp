#include <iostream>
#include <string>

int main()
{
    std::string S, T;
    std::cin >> S >> T;
    std::cout << (S == "AtCoder" && T == "Land"? "Yes":"No");
    return 0;
}