#include <iostream>
#include <vector>

int main()
{
    int X, N, W, Q, P, total_weight;
    std::vector<int> parts_weight = {0}, weight_record;
    std::vector<bool> parts_attached = {false};
    std::cin >> X >> N;

    total_weight = X;

    for (int i = 0; i < N; i++)
    {
        std::cin >> W;
        parts_weight.push_back(W);
        parts_attached.push_back(false);
    }

    std::cin >> Q;

    for (int i = 0; i < Q; i++)
    {
        std::cin >> P;
        if (parts_attached[P])
        {
            total_weight -= parts_weight[P];
            parts_attached[P] = false;
        }
        else
        {
            total_weight += parts_weight[P];
            parts_attached[P] = true;
        }
        weight_record.push_back(total_weight);
    }

    for (size_t i = 0; i < weight_record.size(); i++)
    {
        std::cout << weight_record[i] << '\n';
    }

    return 0;
}