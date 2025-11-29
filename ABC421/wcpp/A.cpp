#include <iostream>
#include <vector>
#include <string>

int main()
{
    int N, X;
    std::string S, Y;
    std::vector <std::string> room = {};
    
    std::cin >> N;

    for (int i=0; i < N; i++)
    {
        std::cin >> S;
        room.push_back(S);
    }

    std::cin >> X >> Y;
    std::cout << (room[X-1] == Y? "Yes":"No");
    return 0;
}