#include<iostream>
#include<cstring>

using namespace std;
int arr[22] = {0};

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n,c;
    int tmp = 0;
    cin>>n;
    for(int i=1;i<=n;i++){
        cin >> arr[0];
        for(int j =1;j<=20;j++){
            cin >> arr[j];
        }
        int cnt = 0;
        for(int k=1;k<20;k++){
            for(int x=1;x<21-k;x++){
                if(arr[x]>arr[x+1]){
                    tmp = arr[x];
                    arr[x] = arr[x+1];
                    arr[x+1]=tmp;
                    cnt++;
                }

            }
        }
        cout << i <<" "<< cnt << "\n";
    }

}