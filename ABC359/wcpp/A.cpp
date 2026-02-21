#include <iostream>
#include <string>

int main()
{
    int N, takahashi = 0;
    std::string S;
    std::cin >> N;
    for (int i = 0; i < N; i++)
    {
        std::cin >> S;
        takahashi += (S == "Takahashi"? 1 : 0);
    }
    std::cout << takahashi;
    return 0;
}