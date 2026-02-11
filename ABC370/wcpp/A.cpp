#include <iostream>

int main()
{
    int L, R;
    std::cin >> L >> R;
    if (L == R)
    {
        std::cout << "Invalid";
    }
    else
    {
        std::cout << (L? "Yes" : "No");
    }
}