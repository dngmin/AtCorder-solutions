#include <iostream>

int main()
{
    int R, X;
    std::cin >> R >> X;
    if (X == 1)
    {
        std::cout << (1600<= R && R <= 2999?"Yes":"No");
    }
    else
    {
        std::cout << (1200 <= R && R <= 2399?"Yes":"No");
    }
    return 0;
}