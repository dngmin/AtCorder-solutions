#include <iostream>
#include <cmath>

int main()
{
    int N;
    int sum = 0;
    std::cin >> N;
    for (int i = 1; i<N+1 ; ++i)
    {
        sum += std::pow(-1,i)*std::pow(i,3);
    }
    std::cout << sum;
    return 0;
}