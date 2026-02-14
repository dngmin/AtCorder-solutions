#include <iostream>

int main()
{
    int N, T, A;
    std::cin >> N >> T >> A;
    std::cout << (N/2 < std::max(T,A)? "Yes" : "No");

    return 0;
}