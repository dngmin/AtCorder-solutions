#include <iostream>
#include <string>

int main()
{
    std::string N;
    int count1 = 1, count2 = 2, count3 = 3;
    std::cin >> N;

    for (size_t i =0; i < N.size(); i++)
    {
        if (N[i] == '1')
        {
            count1 -= 1;
        }
        else if (N[i] == '2')
        {
            count2 -= 1;
        }
        else if (N[i] == '3')
        {
            count3 -= 1;
        }
    }
    std::cout << (!count1 & !count2 & !count3? "Yes":"No");

    return 0;
}