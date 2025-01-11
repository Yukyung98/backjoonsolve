#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    queue<pair<int, int>> q; 
    priority_queue<int> pq; // Max-heap to store priorities

    for (int i = 0; i < priorities.size(); i++) {
        q.push({i, priorities[i]});
        pq.push(priorities[i]);
    }

    while (!q.empty()) {
        auto current = q.front();
        q.pop();

        if (current.second == pq.top()) {
            pq.pop(); 
            answer++; 

            if (current.first == location) {
                return answer;
            }
        } else {
            q.push(current);
        }
    }

    return answer;
}
