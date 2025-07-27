#include <algorithm>
#include <iostream>
#include <limits>
#include <string>
#include <utility>
#include <vector>

const int indians = 6;

const int dist[indians][indians] = {
    {0, 430, 440, 2800, 1200, 540},
    {430, 0, 8, 2900, 1500, 900},
    {440, 8, 0, 2895, 1495, 895},
    {2800, 2900, 2895, 0, 1700, 2300},
    {1200, 1500, 1495, 1700, 0, 660},
    {540, 900, 895, 2300, 660, 0}
};

const std::string cities[] = {
    "Raleigh", "Edison", "Monroe", 
    "Fremont", "Dallas", "Nashville"
};

static std::pair<std::vector<int>, int> computeShortestDistance() {
    std::vector<int> perm{1, 2, 3, 4, 5};
    int min_dist = std::numeric_limits<int>::max();
    std::vector<int> best_path;

    do {
        int total = 0;
        total += dist[0][perm[0]];
        for(int i = 0; i < perm.size() - 1; ++i) {
            total += dist[perm[i]][perm[i + 1]];
        }
        total += dist[perm.back()][0];

        if(total < min_dist) {
            min_dist = total;
            best_path = perm;
        }
    } while(std::next_permutation(perm.begin(), perm.end()));

    return {best_path, min_dist};
}

int main() {
    auto pair = computeShortestDistance();
    const std::vector<int>& path = pair.first;
    int total_distance = pair.second;

    std::cout << "\nShortest route:\n";
    std::cout << cities[0] << " -> ";
    for (int idx : path) {
        std::cout << cities[idx] << " -> ";
    }
    std::cout << cities[0] << '\n';

    std::cout << "Total distance: " << total_distance << " miles\n";
}