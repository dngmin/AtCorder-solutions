#include <iostream>

int main()
{
    double X;
    std::cin >> X;
    if (X >= 38)
    {
        X = 1;
    }
    else if (X < 37.5)
    {
        X = 3;
    }
    else
    {
        X = 2;
    }
    std::cout << X;
    return 0;
}