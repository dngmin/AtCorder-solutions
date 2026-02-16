#include <iostream>
#include <string>

int main()
{
    int N;
    std::string S_now, S_past = "";
    bool can_eat = true;
    std::cin >> N;
    for (int i = 0; i < N; i++)
    {
        std::cin >> S_now;
        if (can_eat && S_now == "sweet" && S_past == "sweet" && i != N-1)
        {
            can_eat = false;
        }
        S_past = S_now;
    }
    
    std::cout << (can_eat? "Yes":"No");

    return 0;
}