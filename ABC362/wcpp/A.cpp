#include <iostream>
#include <string>

int main()
{
    int R, G, B;
    std::cin >> R >> G >> B;
    std::string C;
    std::cin >> C;
    if (C == "Red")
    {
        std::cout << std::min(G,B);
    }
    else if (C == "Green")
    {
        std::cout << std::min(R,B);
    }
    else
    {
        std::cout << std::min(R,G);
    }
    return 0;
}