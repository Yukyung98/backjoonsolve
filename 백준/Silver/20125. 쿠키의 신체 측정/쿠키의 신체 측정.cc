#include <iostream>
#include <string>
#include <map>
using namespace std;
string str;
map<string, int> tt;
int main(){
    int N;
    cin >> N;
    int hartX,hartY;
    int cnt=0;
    int leftL=0 ,rightL =0 ,twice =0;
    int leftR = 0, rightR = 0;
    int flagX = 0, flagLY = 0,flagRY;
    int flag = 0;
    for(int i=1;i<=N;i++){
        cin >>str;
        if(str.find("*_*") != std::string::npos){
            flag = 1;
        }
        for(int j=0;j<N;j++){
            if(str[j]=='*'){
                cnt+=1;
                if(cnt == 1){
                    //심장위치
                    hartX = i+1;
                    hartY = j+1;
                }
                if(cnt>=2 && i == hartX && j<hartY){
                    leftL = cnt-2;
                }
                if (cnt>=2 && i==hartX&& j>(hartY-1)){
                    rightL = cnt - (leftL+2);
                }
                if(i>hartX && j == (hartY -1) &&(leftL||rightL)){
                    twice+=1;
                }
                if(flag ==1){
                    flagLY = hartY-2;
                    flagRY = hartY;
                    if(j==flagLY){
                        leftR++;
                    }
                    if(j == flagRY){
                        rightR++;
                    }
                }
            }
        }
    }
    cout << hartX << " "<<hartY <<"\n";
    cout << leftL << " "<<rightL <<" "<<twice<<" "<<leftR<<" "<<rightR<<"\n";
    
}
 