#include <iostream>
#include <vector>

int main()
{
    int N, K, A;
    std::vector<int> deck;
    std::cin >> N >> K;
    for (int i = 0; i < N; i++)
    {
        std::cin >> A;
        deck.push_back(A);
    }
    for (int i = N - K; i < N; i++)
    {
        std::cout << deck[i] << " ";
    }
    for (int i = 0; i < N - K; i++)
    {
        std::cout << deck[i] << " ";
    }
    return 0;
}