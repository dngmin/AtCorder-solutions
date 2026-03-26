#include <iostream>
#include <string>

int main()
{
    std::string S;
    char main_char;
    std::cin >> S;

    if (S[0] == S[1])
    {
        main_char = S[0];
    }
    else
    {
        main_char = (S[0] == S[2]? S[0] : S[1]);
    }
    for (size_t i = 0; i < S.size(); i++)
    {
        if (S[i] != main_char)
        {
            std::cout << S[i];
            return 0;
        }
    }

}