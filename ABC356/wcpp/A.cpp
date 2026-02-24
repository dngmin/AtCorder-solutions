#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int N, L, R;
    std::vector<int> A_list;
    std::cin >> N >> L >> R;
    for (int i = 1; i < N+1; i++)
    {
        A_list.push_back(i);
    }
    std::reverse(A_list.begin()+L-1,A_list.begin()+R);
    for (int i = 0; i < N; i++)
    {
        std::cout << A_list[i] << " ";
    }
    return 0;
}