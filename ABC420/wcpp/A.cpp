#include <iostream>

int main()
{
    int X,Y;
    std::cin >> X >> Y;
    std::cout << ((X+Y)%12 == 0? 12 : (X+Y)%12);
    return 0;
}