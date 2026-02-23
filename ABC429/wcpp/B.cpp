#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int N, M, A;
    std::vector<int> A_list;
    std::cin >> N >> M;
    for (int i = 0; i < N; i++)
    {
        std::cin >> A;
        A_list.push_back(A);
        M -= A;
    }
    std::cout << (std::find(A_list.begin(),A_list.end(),-M) != A_list.end()? "Yes":"No");
    return 0;
}