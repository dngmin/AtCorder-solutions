#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main()
{
    std::string X;
    int zero = 0;
    std::vector <int> X_element;
    std::cin >> X;
    
    for (int i = 0; i < X.size(); i++)
    {
        if (X[i] == '0')
        {
            zero += 1;
        }
        else
        {
        X_element.push_back(X[i] - '0');
        }
    }
    std::sort(X_element.begin(), X_element.end());

    for (int i = 0; i < X_element.size(); i++)
    {
        std::cout << X_element[i];
        if (i == 0)
        {
            std::cout << std::string(zero, '0');
        }
    }

    return 0;
}