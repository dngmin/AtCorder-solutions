#include <iostream>

int main()
{
    int N, C, T, last_candy_time, candy = 1;
    std::cin >> N >> C >> last_candy_time;

    for (int i = 1; i < N; i++)
    {
        std::cin >> T;
        if (T-last_candy_time >= C)
        {
            last_candy_time = T;
            candy += 1;
        }

    }
    std::cout << candy;

    return 0;
}