#include <iostream>

int main()
{
    int N, A, B;
    int count = 0;
    std::cin >> N;
    for (int i = 0; i < N; i++)
    {
        std::cin >> A >> B;
        count += (B > A? 1 : 0);
    }
    std::cout << count;
    return 0;
}