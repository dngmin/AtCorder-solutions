#include <iostream>

int main()
{
    int A1,A2,A3;
    std::cin >> A1 >> A2 >> A3;
    std::cout << (A1*A2 == A3 || A1*A3==A2 || A2*A3==A1?"Yes":"No");
    return 0;
}