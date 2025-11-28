#include <iostream>
#include <string>

int main()
{
    std::string S;
    int world, stage;
    std::cin >> S;
    world = S[0] - '0';
    stage = S[2] - '0';
    std::cout << (stage == 8? world+1:world) << "-" << (stage == 8? 1:stage+1);
    return 0;
}