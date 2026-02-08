#include <iostream>
#include <string>

int main()
{
    int output = 0;
    std::string S;
    for (int i =1; i < 13; i++)
    {
        std::cin >> S;
        output += (S.size() == i? 1 : 0);
    }
    std::cout << output;

    return 0;
}