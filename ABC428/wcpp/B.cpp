#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

int main()
{
    int N, K, times = 0;
    std::string S;
    std::set<std::string> ts, output;
    std::vector<std::string> tv;
    std::cin >> N >> K >> S;
    for (int i = 0; i + K <= N; i++)
    {
        ts.insert(S.substr(i,K));
        tv.push_back(S.substr(i,K));
    }
    for (std::string t : ts)
    {
        if (std::count(tv.begin(), tv.end(), t) > times)
        {
            times = std::count(tv.begin(), tv.end(), t);
            output = {t};
        }
        else if (std::count (tv.begin(), tv.end(), t) == times)
        {
            output.insert(t);
        }
    }
    std::cout << times << "\n";
    for (std::string o : output)
    {
        std::cout << o << " ";
    }
    return 0;
}