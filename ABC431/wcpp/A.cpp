#include <iostream>

int main()
{
    int H,B;
    std::cin >> H >> B;
    if (H>B)
        std::cout << H-B;
    else
        std::cout << 0;
    return 0;
}