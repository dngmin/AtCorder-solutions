#include <iostream>

int main()
{
    int N, A, sum = 0;
    std::cin >> N;
    for (int i = 0; i < N-1; i++)
    {
        std::cin >> A;
        sum -= A;
    }
    std::cout << sum;
    return 0;
}