#include <iostream>
#include <string>
using namespace std;
string str;
int main(){
    string tt = "aeiou";
    string alpt = "bcdfghjklmnpqrstvwxyz";
    while(1){
        cin >> str;
        if (str == "end"){
            break;
        }
        int flag1 = 0;
        for(char a : str){
            for(char ss : tt){
                if(a == ss){
                    flag1 = 1;
                    break;
                }
            }
        }
        if(flag1 == 0){
            cout << "<" << str << ">" << " is not acceptable. \n";
        } else{
            for(int i=0;i<str.length();i++){
                if(str[i]==str[i+1]&& str[i]!='o' && str[i]!='e'){
                    flag1 = 3;
                    break;
                }
            }
            if(str.length()>=3){
            for(int i=0;i<str.length()-2;i++){
                if(tt.find(str[i])!= std::string::npos&&tt.find(str[i+1])!= std::string::npos&&tt.find(str[i+2])!= std::string::npos||alpt.find(str[i])!= std::string::npos&&alpt.find(str[i+2])!= std::string::npos&&alpt.find(str[i+1])!= std::string::npos){
                    flag1=2;
                    break;
                } 
            }}
             if(flag1 != 1){
            cout << "<" << str << ">" << " is not acceptable. \n";
            } else{
                cout << "<" << str << ">" << " is acceptable. \n";
            }
        }
       
    }
    
}
 