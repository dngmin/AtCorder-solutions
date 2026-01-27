#include <iostream>
#include <string>

int main()
{
    int N;
    char c1, c2;
    std::string S;
    
    std::cin >> N >> c1 >> c2 >>S;

    for (int i = 0; i < S.size(); i++)
    {
        std::cout << (S[i] == c1? c1:c2);
    }
    
    return 0;
}