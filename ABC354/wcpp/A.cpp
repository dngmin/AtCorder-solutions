#include <iostream>
#include <cmath>

int main()
{
    int H, plant = 1, day = 1;
    std::cin >> H;
    while (plant <= H)
    {
        plant += pow(2, day);
        day++;
    }
    std::cout << day;
    return 0;
}