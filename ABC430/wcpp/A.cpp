#include <iostream>

int main()
{
    int A, B, C, D;
    std::cin >> A >> B >> C >> D;
    if (C>=A && D<B)
    {
        std::cout << "Yes";
    }
    else{
        std::cout << "No";
    }
    return 0;
}