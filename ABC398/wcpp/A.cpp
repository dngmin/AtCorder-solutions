#include <iostream>
#include <string>

int main()
{
    int N;
    std::string equal, hyphen = "";
    std::cin >> N;
    equal = (N%2 == 0? "==":"=");
    for (int i = 0; i < (N-1)/2; i++)
    {
        hyphen += "-";
    }
    std::cout << hyphen + equal + hyphen;
    return 0;
}