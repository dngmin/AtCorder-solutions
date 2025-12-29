#include <iostream>

int main()
{
    int N, A, A1 = 0, A2 = 0;
    std::cin >> N;
    for (int i = 0; i < N; i++)
    {
        std::cin >> A;
        if (A == A1 && A == A2)
        {
            std::cout << "Yes";
            return 0;
        }
        A2 = A1;
        A1 = A;
    }
    std::cout << "No";
    return 0;
}