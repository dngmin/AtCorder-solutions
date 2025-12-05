#include <iostream>
#include <vector>
#include <algorithm>
int main()
{
    int N, A, X;
    std::vector <int> A_list = {};
    std::cin >> N;
    for (int i =0; i<N;i++)
    {
        std::cin >> A;
        A_list.push_back(A);
    }
    std::cin >> X;
    std::cout << (std::find(A_list.begin(),A_list.end(),X) == A_list.end()?"No":"Yes");
    return 0;
}