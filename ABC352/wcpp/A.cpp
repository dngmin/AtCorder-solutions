#include <iostream>

int main()
{
    int N, X, Y, Z;
    std::cin >> N >> X >> Y >> Z;
    std::cout << (std::min(X,Y)<Z && Z<std::max(X,Y)? "Yes":"No");
    return 0;
}