#include <iostream>

int main()
{
    int A, B;
    std::cin >> A >> B;
    for (int i = 0; i <= 9; i++)
    {
        if (i != A && i != B) 
        {
            std::cout << i;
            return 0;
        }
    }
}