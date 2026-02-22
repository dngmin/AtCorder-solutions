#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

int main()
{
    int N, M;
    std::cin >> N >> M;
    std::vector<std::string> grid(N);
    std::string subgrid;
    std::unordered_set<std::string> subgrid_set;
    for (int i = 0; i < N; i++)
    {
        std::cin >> grid[i];
    }
    for (int i = 0; i < N-M+1; i++)
    {
        for (int j = 0; j < N-M+1; j++)
        {
            subgrid = "";
            for (int k = 0; k < M; k++)
            {
                subgrid += grid[i+k].substr(j,M);
                // subgrid = grid[i+k].substr(j,M);
            }
            subgrid_set.insert(subgrid);
        }
    }
    std::cout << subgrid_set.size();
    return 0;
}