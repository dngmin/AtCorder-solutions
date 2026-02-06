#include <iostream>
#include <string>

int main()
{
    std::string S;
    std::cin >> S;
    std::cout << (S.substr(S.size()-3,3) == "san"? "Yes":"No");
    
    return 0;
}