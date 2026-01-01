#include <iostream>
#include <string>

int main()
{
    std::string S1,S2;
    int which;
    std::cin >> S1 >> S2;
    if (S1 == "sick" && S2 == "sick")
    {
        which = 1;
    }
    else if (S1 == "sick" && S2 == "fine")
    {
        which = 2;
    }
    else if (S1 == "fine" && S2 == "sick")
    {
        which = 3;
    }
    else
    {
        which = 4;
    }
    std::cout << which;
    return 0;
}