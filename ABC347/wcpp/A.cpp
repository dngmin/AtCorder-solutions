#include <iostream>
#include <vector>

int main()
{
    int N, K, A;
    std::cin >> N >> K;
    for (int i = 0; i < N; i++)
    {
        std::cin >> A;
        if (A%K==0)
        {
            std::cout << A/K << " ";
        }
    }
    return 0;
}