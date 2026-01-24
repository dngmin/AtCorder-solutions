#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int A, B, C, D;
    std::cin >> A >> B >> C >> D;
    std::vector<int> deck = {A, B, C, D};

    std::sort(deck.begin(),deck.end());
    deck.erase(std::unique(deck.begin(),deck.end()),deck.end());

    std::cout << (deck.size() == 2? "Yes":"No");

    return 0;
}