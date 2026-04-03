#include <iostream>

int main()
{
    int N, threshold = -1;
    std::cin >> N;
    for (; N > 0; N /= 10)
    {
        if (N%10 <= threshold)
        {
            std::cout << "No";
            return 0;
        }
        threshold = N%10;
    }
    std::cout << "Yes";
    return 0;
}