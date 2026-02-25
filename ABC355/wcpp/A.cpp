#include <iostream>

int main()
{
    int A, B;
    std::cin >> A >> B;
    std::cout << (A == B? -1 : 6-A-B);
    return 0;
}