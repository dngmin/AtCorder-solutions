#include <iostream>
#include <string>

int main()
{
    std::string S;
    int count2 = 0;
    std::cin >> S;
    for (int i = 0; i < S.length(); i++)
    {
        count2 += (S[i] == '2'?1:0);
    }
    std::cout << std::string(count2,'2');
    return 0;
}