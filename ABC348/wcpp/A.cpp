#include <iostream>

int main()
{
    int N;
    std::cin >> N;
    for (int i = 0; i < N/3; i++)
    {
        std::cout << "oox";
    }
    for (int i = 0; i < N%3; i++)
    {
        std::cout << "o";
    }
    return 0;
}