#include <iostream>

int main()
{
    int N, L, A, passed = 0;
    std::cin >> N >> L;
    for (int i = 0; i < N; i++)
    {
        std::cin >> A;
        passed += (A >= L? 1 : 0);
    }
    std::cout << passed << std::endl;
    return 0;
}