#include <iostream>
#include <vector>

int main()
{
    int N, K, X, A;
    std::cin >> N >> K >> X;
    std::vector<int> A_list;
    for (int i = 0; i < N; i++)
    {
        std::cin >> A;
        A_list.push_back(A);
        if (i == K-1)
        {
            A_list.push_back(X);
        }
    }
    for (size_t i = 0; i < A_list.size(); i++)
    {
        std::cout << A_list[i] << " ";
    }

    return 0;
}