#include <iostream>
#include <string>
#include <map>
using namespace std;
string str;
map<string, int> tt;
int main(){
    int N;
    string Game;
    cin >> N >>Game;
    for(int i=0;i<N;i++){
        cin>> str;
        tt[str] = 1;
    }
    if(Game == "Y"){
        cout << tt.size();
    }else if(Game=="F"){
        cout << tt.size()/2;
    }else{
        cout << tt.size()/3;
    }
    
}
 