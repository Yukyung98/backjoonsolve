#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

int solution(vector<vector<string>> clothes) {
     unordered_map<string, int> clothe;
    for (auto& k : clothes) {
        clothe[k[1]] += 1;
    }

    int answer = 1;

    for (auto& c : clothe) {
        answer *= (c.second + 1); 
    }
    return answer - 1; 
}