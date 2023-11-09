#include <bits/stdc++.h>
using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    //answer.push_back(arr[0]);
    for(int i = 0; i < arr.size(); i++){
        int k = i+1;
        if(k==arr.size()){
            answer.push_back(arr[i]);
        } else{
            if(arr[i] == arr[k])
            {
            continue;
            }
            else{
                answer.push_back(arr[i]);
            }
        }
        
    }
    return answer;
}