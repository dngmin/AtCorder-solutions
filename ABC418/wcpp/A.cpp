#include <iostream>
#include <string>

int main()
{
    int N;
    std::string S;

    std::cin >> N >> S;
    if (N<3)
    {
        std::cout << "No";
    }
    else
    {
        std::cout << (S.substr(N-3,N)=="tea"?"Yes":"No");
    }
    return 0;
}