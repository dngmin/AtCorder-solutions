#include <iostream>

int main()
{
    int A, B, output = 0;
    std::cin >> A >> B;
    if (A == B)
    {
        output += 1;
    }
    else
    {
        output += 2 + ((A-B)%2 == 0? 1 : 0);
    }
    std::cout << output;

    return 0;
}