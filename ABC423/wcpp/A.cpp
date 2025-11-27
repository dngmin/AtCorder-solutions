#include <iostream>

int main()
{
    int X,C;
    std::cin >> X >> C;
    std::cout << X / (1000+C) * 1000;
    return 0;
}