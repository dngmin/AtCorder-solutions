#include <iostream>

int main()
{
    int N, A, sum = 0;
    std::cin >> N;
    for (int i = 0; i < N/2; i++)
    {
        std::cin >> A;
        sum += A;
        std::cin >> A;
    }
    if (N%2 == 0)
    {
        std::cout << sum;
    }
    else
    {
        std::cin >> A;
        std::cout << sum + A;
    }
    return 0;
}