#include <iostream>

int main()
{
    int A, B, C, can;
    std::cin >> A >> B >> C;

    if (B < C)
    {
        can = (B < A && A < C? 0 : 1);
    }
    else
    {
        can = (C < A && A < B? 1 : 0);
    }
    std::cout << (can? "Yes" : "No");

    return 0;
}