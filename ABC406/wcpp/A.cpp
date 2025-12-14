#include <iostream>

int main()
{
    int A, B, C, D;
    std::cin >> A >> B >> C >> D;
    std::cout << (C<A || (C==A && D<B)?"Yes":"No");
    return 0;
}