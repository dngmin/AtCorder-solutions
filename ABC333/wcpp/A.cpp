#include <iostream>
#include <string>

int main()
{
    int N;
    std::cin >> N;
    char c = N + '0';
    std::cout << std::string(N, c) << std::endl;
    return 0;
}