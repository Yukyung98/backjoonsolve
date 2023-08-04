#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
#include<stack>
#include<string>
#define MAX 1000000
int arr[MAX] = { 0 };
using namespace std;
long long N,M;
long long x=0,y=0;
long long a,b;

void isPrime() {
	for (int i = 2; i * i <= MAX; i++) {
		if (arr[i] == 0) {
			for (int j = i * i; j <= MAX; j += i) {
				arr[j] = 1;
			}
		}
	}
}
int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);
	isPrime();
	while (1) {
		cin >> N;
		if (N == 0) {
			break;
		}
		bool ck = false;
		for (int i = 3; i <= N; i += 2) {
			if (arr[i] == 0 && arr[N - i] == 0) {
				cout << N << " = " << i << " + " << N-i<<"\n";
				ck = true;
				break;
			}
		}
		if (!ck) {
		cout << "Goldbach's conjecture is wrong.\n";
		}
	}
}