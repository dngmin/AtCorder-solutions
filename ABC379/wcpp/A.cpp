#include <iostream>
#include <string>

int main()
{
    std::string N;
    std::cin >> N;
    char a = N[0], b = N[1], c = N[2];

    std::cout << b << c << a << ' ' << c << a << b;

    return 0;
}