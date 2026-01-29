#include <iostream>
#include <string>
#include <algorithm>

int main()
{
    int N, D, cookie;
    std::string S;
    std::cin >> N >> D >> S;
    std::cout << std::count(S.begin(),S.end(),'.') + D;
    return 0;
}