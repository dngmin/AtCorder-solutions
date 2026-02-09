#include <iostream>

int main()
{
    char SAB, SAC, SBC;
    std::cin >> SAB >> SAC >> SBC;

    if (SAB == '>')
    {
        if (SAC == '>')
        {
            std::cout << (SBC == '>'? 'B' : 'C');
        }
        else
        {
            std::cout << 'A';
        }
    }
    else
    {
        if (SAC == '>')
        {
            std::cout << 'A';
        }
        else
        {
            std::cout << (SBC == '>'? 'C' : 'B');
        }
    }

    return 0;
}