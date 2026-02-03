#include <iostream>
#include <string>
#include <set>

int main()
{
    std::string S;
    std::set ABC = {'A','B','C'};
    std::set<char> S_element;
    std::cin >> S;
    for (int i = 0; i < 3; i++)
    {
        S_element.insert(S[i]);
    }
    std::cout << (S_element == ABC? "Yes":"No");

    return 0;
}