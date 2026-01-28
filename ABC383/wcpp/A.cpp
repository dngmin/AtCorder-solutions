#include <iostream>

int main()
{
    int N, T, V, time, water = 0, T_past = 0;
    std::cin >> N;
    for (int i = 0; i < N; i ++)
    {
        std::cin >> T >> V;
        time = T - T_past;
        T_past = T;
        water = (water - time <= 0? 0 : water - time) + V;
    }
    std::cout << water;

    return 0;
}