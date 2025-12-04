#include <iostream>
#include <string>

int main()
{
    int N, L, R;
    std::string S, cut;
    std::cin >> N >> L >> R >> S;
    cut = S.substr(L-1,R-L+1);
    std::cout << (cut.find("x")==std::string::npos?"Yes":"No");
    return 0;
}