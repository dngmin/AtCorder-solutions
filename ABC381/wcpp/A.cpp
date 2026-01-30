#include <iostream>
#include <string>

int main()
{
    int N;
    std::string S;
    std::cin >> N >> S;
    int middle_idx = ((N + 1) / 2) - 1;

    if (S.substr(0, middle_idx) == std::string(middle_idx,'1'))
    {
        if (S[middle_idx] == '/')
        {
            if (S.substr(middle_idx+1) == std::string(middle_idx, '2'))
            {
                std::cout << "Yes";
                return 0;
            }
        }
    }
    std::cout << "No";

    return 0;
}