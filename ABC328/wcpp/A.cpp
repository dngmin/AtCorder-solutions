#include <iostream>

int main()
{
    int N, X, S, total = 0;
    std::cin >> N >> X;
    for (int i = 0; i < N; i++)
    {
        std::cin >> S;
        if (S  <= X) total += S;
    }
    std::cout << total;
    return 0;
}