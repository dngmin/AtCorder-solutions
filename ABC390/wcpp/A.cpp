#include <iostream>
#include <vector>

int main()
{
    int A,count0 = 0, count1 = 0, count_1 = 0;
    std::vector A_list = {1,2,3,4,5};
    for (int i = 0; i < 5; i++)
    {
        std::cin >> A;
        if (A_list[i]-A == 0)
        {
            count0 += 1;
        }
        else if (A_list[i]-A == 1)
        {
            count1 += 1;
        }
        else if (A_list[i]-A == -1)
        {
            count_1 += 1;
        }
        else
        {
            break;
        }
    }
    std::cout << (count0 == 3 && count1 == 1 && count_1 == 1?"Yes":"No");
    return 0;
}