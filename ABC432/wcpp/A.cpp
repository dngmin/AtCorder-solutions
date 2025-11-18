#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int A,B,C;
    std::cin >> A >> B >> C;

    std::vector<int> v = {A,B,C};
    std::sort(v.begin(),v.end(),std::greater<int>());

    for (int x : v) std::cout << x;

    return 0;
}