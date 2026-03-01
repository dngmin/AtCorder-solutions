#include <iostream>

int main()
{
    int A, B, team_t = 0, team_a = 0;
    for (int i = 0; i < 9; i++)
    {
        std::cin >> A;
        team_t += A;
    }
    for (int i = 0; i < 8; i++)
    {
        std::cin >> B;
        team_a += B;
    }
    std::cout << team_t - team_a + 1;
    return 0;
}