#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue<int> q;
    for(int i=0;i<speeds.size();i++){
        int cnt = 0;
        while(progresses[i]<100){
            cnt++;
            progresses[i]+=speeds[i];
        }
        q.push(cnt);
    }
    int cnt2 = 0;
    int max = 0;
    while (!q.empty()) {
        int a = q.front();
        cnt2++;
        q.pop();
        if(a>max){
            max = a;
        }
        if(max<q.front()){
            answer.push_back(cnt2);
            cnt2 =0;
        } else if(q.empty()){
            answer.push_back(cnt2);
        }
        

	}
    return answer;
}
