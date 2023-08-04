#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
#include<stack>
#include<string>

using namespace std;
unsigned long long N;
unsigned long long x,y;

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);
	cin >> N;
	for (int i = 5; i <= N; i *= 5) {
		x += N / i;
	}
	cout << x;
	

}