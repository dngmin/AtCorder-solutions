#include <iostream>

int main()
{
    int N, A, past_A;
    std::cin >> N >> past_A;
    for (int i = 1; i < N; i++)
    {
        std::cin >> A;
        if (past_A >= A)
        {
            std::cout << "No";
            return 0;
        }
        past_A = A;
    }
    std::cout << "Yes";
    return 0;
}