#include <iostream>

int main()
{
    int N, A, a;
    std::cin >> N >> A;
    for (int i = 1; i < N; i++)
    {
        std::cin >> a;
        if (A != a)
        {
            std::cout << "No";
            return 0;
        }
    }
    std::cout << "Yes";
    return 0;
}