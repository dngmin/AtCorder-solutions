#include <iostream>
#include <string>

int main()
{
    std::string S;
    int dot_index;
    std::cin >> S;
    for (size_t i = 0; i < S.size(); i++)
    {
        if (S[i] == '.') dot_index = i;
    }
    std::cout << S.substr(dot_index+1,-1);
    return 0;
}