#include <iostream>
#include <stack>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
double  H,W,N,M ; 
int arr[3];
int main(){
    while(1){
        cin >> arr[0]>>arr[1]>>arr[2];
        if(arr[0]==0&&arr[2]==0&&arr[1]==0){
            break;
        } else{
            sort(arr,arr+3);
            if(arr[0] == arr[1] && arr[1] == arr[2]){
                cout << "Equilateral"<<endl;
            } else{
                if(arr[2]>=arr[0]+arr[1]){
                    cout << "Invalid"<<endl;
                }else if(arr[1]==arr[0]||arr[1]==arr[2]){
                    cout << "Isosceles"<<endl;
                }
                else{
                    cout << "Scalene "<<endl;
                }
            }
        }

    }
    
    
}
    