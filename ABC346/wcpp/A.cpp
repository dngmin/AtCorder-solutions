#include <iostream>

int main()
{
    int N, A1, A2;
    std::cin >> N >> A1;
    for (int i = 1; i < N; i++)
    {
        std::cin >> A2;
        std::cout << A1 * A2 << " ";
        A1 = A2;
    }
    return 0;
}