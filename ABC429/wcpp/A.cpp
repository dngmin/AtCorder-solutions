#include <iostream>

int main()
{
    int N,M;
    std::cin >> N >> M;
    for(int i=1;i<=N;++i)
    {
        if (i<=M)
        {
            std::cout << "OK" << "\n";
        }
        else
        {
            std::cout << "Too Many Requests" << "\n";
        }
    }
    
    return 0;
}