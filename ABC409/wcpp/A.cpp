#include <iostream>
#include <string>

int main()
{
    int N;
    std::string T, A;
    std::cin >> N >> T >> A;
    bool both = false;

    for (int i = 0; i < N; i ++)
    {
        if (T[i] == 'o' && A[i] == 'o')
        {
            both = true;
            break;
        }
    }
    std::cout << (both?"Yes":"No");
    return 0;
}