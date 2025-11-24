#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int main()
{
    std::vector<std::string> OS = {"Ocelot","Serval","Lynx"};
    std::string X,Y;
    int X_idx,Y_idx;
    std::cin >> X >> Y;
    X_idx = std::find(OS.begin(),OS.end(),X)-OS.begin();
    Y_idx = std::find(OS.begin(),OS.end(),Y)-OS.begin();
    std::cout << (X_idx >= Y_idx ? "Yes" : "No");
    return 0;
}