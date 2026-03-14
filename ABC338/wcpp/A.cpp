#include <iostream>
#include <string>

int main()
{
    std::string S;
    std::cin >> S;
    int ascii = S[0];
    if (ascii > 90)
    {
        std::cout << "No";
        return 0;
    }
    for (int i = 1; i < S.size(); i++)
    {
        int ascii = S[i];
        if (ascii <= 90)
        {
            std::cout << "No";
            return 0;
        }
    }
    std::cout << "Yes";
    return 0;
}