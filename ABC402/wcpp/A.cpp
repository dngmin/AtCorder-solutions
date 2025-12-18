#include <iostream>
#include <string>

int main()
{
    std::string S, output;
    std::cin >> S;
    for (size_t i = 0; i < S.size(); i++)
    {
        if ('A' <= S[i] && S[i] <= 'Z')
        {
            output += S[i];
        }
    }
    std::cout << output;
    return 0;
}