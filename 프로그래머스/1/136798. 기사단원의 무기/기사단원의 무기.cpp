#include <string>
#include <vector>
#include <iostream>
#include <cmath>
using namespace std;

int solution(int number, int limit, int power) {
    int answer = 0;
    int cnt = 0;
    vector<int> cc;
    for(int i = 1;i<=number;i++){
        for(int j = 1; j*j <= i ; j++){
            if(i%j == 0){
                cnt++;
                if(j*j < i)
                    cnt++;                
            }
        }        
        if(cnt>limit){
            answer += power;
        } else{
            answer += cnt;
        }
        cnt = 0;
    }
    
    return answer;
}