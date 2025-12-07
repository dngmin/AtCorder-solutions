#include <iostream>

int main()
{
    int N, M, A;
    int total = 0;
    std::cin >> N >> M;
    for (int i = 0;i<N;i++)
    {
        std::cin >> A;
        total += A;
    }
    std::cout << (total <= M?"Yes":"No");

    return 0;
}