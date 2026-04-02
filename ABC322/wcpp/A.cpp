#include <iostream>
#include <string>

int main()
{
    int N;
    std::string S;
    std::cin >> N >> S;
    for (int i = 0; i < N-2; i++)
    {
        if (S[i] == 'A' && S[i+1] == 'B' && S[i+2] == 'C')
        {
            std::cout << i+1;
            return 0;
        }
    }
    std::cout << -1;
    return 0;
}