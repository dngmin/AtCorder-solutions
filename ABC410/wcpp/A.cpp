#include <iostream>
#include <vector>

int main()
{
    int N, K, A;
    int answer = 0;
    std::vector <int> A_list;
    std::cin >> N;
    for (int i = 0; i < N; i++)
    {
        std::cin >> A;
        A_list.push_back(A);
    }
    std::cin >> K;
    for (int i = 0; i < N; i++)
    {
        answer += (A_list[i]>=K?1:0);
    }
    std::cout << answer;
}