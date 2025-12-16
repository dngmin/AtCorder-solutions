#include <iostream>
#include <string>

int main()
{
    std::string S, alphabet = "abcdefghijklmnopqrstuvwxyz";
    std::cin >> S;
    for (int i = 0; i < 26; i++)
    {
        if (S.find(alphabet[i]) == std::string::npos)
        {
            std::cout << alphabet[i];
            return 0;
        }
    }
}