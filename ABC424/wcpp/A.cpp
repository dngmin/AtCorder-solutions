#include <iostream>

int main()
{
    int a,b,c;
    std::cin >> a >> b >> c;
    std::cout << (a == b or a == c or b == c? "Yes" : "No");
    return 0;
}