#include <iostream>

int main()
{
    int N, H, H1;
    std::cin >> N >> H1;
    for (int i = 2; i <= N; i++)
    {
        std::cin >> H;
        if (H > H1)
        {
            std::cout << i;
            return 0;
        }
    }
    std::cout << -1;
    return 0;
}