#include <iostream>
#include <string>

int main()
{
    int N, count = 0;
    std::string S;
    std::cin >> N >> S;
    for (int i = 0; i < N-1; i++)
    {
        count += (S[i] == '#' && S[i+2] == '#' && S[i+1] == '.'? 1 : 0);
    }
    std::cout << count;
    
    return 0;
}