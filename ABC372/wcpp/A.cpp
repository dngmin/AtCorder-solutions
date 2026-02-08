#include <iostream>
#include <string>

int main()
{
    std::string S;
    std::cin >> S;
    for (char s : S)
    {
        if (s != '.')
        {
            std::cout << s;
        }
    }
    return 0;
}