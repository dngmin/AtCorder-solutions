#include <iostream>
#include <vector>

int main()
{
    int N, A;
    std::cin >> N;
    std::vector<int> output(N), number(N+1,0);
    
    for (int i = 0; i < N; i++)
    {
        std::cin >> A;
        output[i] = A;
        if (A != -1)
        {
            if (number[A] == A)
            {
                std::cout << "No";
                return 0;
            }
            number[A] = A;
        }
    }
    for (int i = 0; i < N; i++)
    {
        if (output[i] == -1)
        {
            for (int j = 1; j <= N; j++)
            {
                if (std::find(number.begin(),number.end(),j) == number.end())
                {
                    output[i] = j;
                    number.push_back(j);
                    break;
                }
            }
        }
    }
    std::cout << "Yes" << std::endl;
    for (int i = 0; i < N; i++)
    {
        std::cout << output[i] << ' ';
    }
}