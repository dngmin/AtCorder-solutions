#include <iostream>
#include <string>
#include <map>

int main()
{
    std::string D;
    std::map<std::string,std::string> oppsite;
    oppsite["N"] = "S";
    oppsite["E"] = "W";
    oppsite["W"] = "E";
    oppsite["S"] = "N";
    oppsite["NE"] = "SW";
    oppsite["NW"] = "SE";
    oppsite["SE"] = "NW";
    oppsite["SW"] = "NE";
    std::cin >> D;
    std::cout << oppsite[D];
    
    return 0;
}