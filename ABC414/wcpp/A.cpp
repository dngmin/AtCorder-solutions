#include <iostream>

int main()
{
    int N, L, R, X, Y;
    int full_listener = 0;
    std::cin >> N >> L >> R;
    for (int i =0; i < N; i++)
    {
        std::cin >> X >> Y;
        full_listener += (X<=L && Y>=R?1:0);
    }
    std::cout << full_listener;
    return 0;
}