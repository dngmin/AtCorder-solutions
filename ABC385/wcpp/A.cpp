#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int A, B, C;
    std::cin >> A >> B >> C;
    std::vector<int> group = {A, B, C};
    std::sort(group.begin(),group.end());
    std::cout << (group[0]+group[1]==group[2]|(A==B&A==C)? "Yes":"No");

    return 0;
}