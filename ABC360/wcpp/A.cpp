#include <iostream>
#include <string>

int main()
{
    std::string S;
    std::cin >> S;
    std::cout << (S=="RMS"||S=="RSM"||S=="SRM"?"Yes":"No");
    return 0;
}