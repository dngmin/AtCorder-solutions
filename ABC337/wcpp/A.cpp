#include <iostream>

int main()
{
    int N, X, Y, t = 0, a = 0;
    std::cin >> N;
    for (int i = 0; i < N; i++)
    {
        std::cin >> X >> Y;
        t += X;
        a += Y;
    }
    if (t == a) std::cout << "Draw";
    else std::cout << (t > a? "Takahashi":"Aoki");
    return 0;
}