#include <iostream>
#include <string>

int main()
{
 std::string S;
 std::cin >> S;

 std::cout << S.substr(0,(S.length()+1)/2-1) << S.substr((S.length())/2+1);
 return 0;
}