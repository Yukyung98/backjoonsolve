#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(string my_string, int n) {
    string answer = "";
    for(char i : my_string){
        answer += string(n,i);
    }
    return answer;
}