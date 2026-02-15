#include <iostream>

int main()
{
    int Y;
    std::cin >> Y;
    if (Y%400 == 0)
    {
        std::cout << 366;
    }
    else if (Y%100 == 0)
    {
        std::cout << 365;
    }
    else if (Y%4 == 0)
    {
        std::cout << 366;
    }
    else
    {
        std::cout << 365;
    }

    return 0;
}