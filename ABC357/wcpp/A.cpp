#include <iostream>

int main()
{
    int N, M, H, count = 0;
    std::cin >> N >> M;
    for (int i = 0; i < N; i++)
    {
        std::cin >> H;
        M -= H;
        count += (M >= 0? 1:0);
    }
    std::cout << count;
    return 0;
}