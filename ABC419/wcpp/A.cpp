#include <iostream>
#include <string>
#include <unordered_map>

int main()
{
    std::string S;
    std::unordered_map <std::string, std::string> color;
    color["red"] = "SSS";
    color["blue"] = "FFF";
    color["green"] = "MMM";

    std::cin >> S;

    if (color.count(S))
    {
        std::cout << color[S];
    }
    else
    {
        std::cout << "Unknown";
    }
    return 0;
}