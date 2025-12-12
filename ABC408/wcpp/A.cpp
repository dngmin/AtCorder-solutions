#include <iostream>

int main()
{
    int N, S;
    int past_T = 0;
    int current_T;
    bool awake = true;

    std::cin >> N >> S;
    for (int i = 0; i < N; i++)
    {
        std::cin >> current_T;
        if (current_T - past_T > S)
        {
            awake = false;
            break;
        }
        past_T = current_T;
    }
    std::cout << (awake?"Yes":"No");

    return 0;
}