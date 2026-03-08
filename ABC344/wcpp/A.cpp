#include <iostream>
#include <string>

int main()
{
    std::string S;
    bool print = true;
    std::cin >> S;
    for (char s : S)
    {
        if (s == '|')
        {
            print = (print? false:true);
            continue;
        }
        if (print) std::cout << s;
    }
    return 0;
}