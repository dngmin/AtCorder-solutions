#include <iostream>

int main()
{
    int S,A,B,X;
    std::cin >> S >> A >> B >> X;
    if ((X%(A+B))>A)
    {
        std::cout << (X/(A+B)+1)*A*S;
    }
    else{
        std::cout << (X/(A+B))*A*S + (X%(A+B))*S;
    }
    return 0;
}