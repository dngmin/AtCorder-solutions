#include <iostream>
#include <string>

int main()
{
    int N, A, B;
    std::string S;
    std::cin >> N >> A >> B >> S;
    std::cout << S.substr(A,N-A-B);
    return 0;
}