#include <iostream>

int main()
{
    int A, B;
    std::cin >> A >> B;
    std::cout << (long) (pow(A,B) + pow(B,A));
    return 0;
}