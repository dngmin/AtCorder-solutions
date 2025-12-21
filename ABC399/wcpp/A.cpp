#include <iostream>
#include <string>

int main()
{
    int N, Hamming_Distance = 0;
    std::string S, T;
    std::cin >> N >> S >> T;

    for (int i =0; i < N; i++)
    {
        Hamming_Distance += (S[i] == T[i]?0:1);
    }
    std::cout << Hamming_Distance;

    return 0;
}