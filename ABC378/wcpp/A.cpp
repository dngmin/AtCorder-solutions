#include <iostream>
#include <vector>

int main()
{
    int A, output = 0;
    std::vector<int> balls = {0,0,0,0,0};
    for (int i = 0; i < 4; i ++)
    {
        std::cin >> A;
        balls[A] += 1;
    }
    for (int i = 1; i < 5; i++)
    {
        if (balls[i] == 2 | balls[i] == 3)
        {
            output += 1;
        }
        else if (balls[i] == 4)
        {
            output += 2;
        }
    }
    std::cout << output;

    return 0;
}