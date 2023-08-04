#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
#include<stack>
#include<string>

using namespace std;
unsigned long long N,M;
unsigned long long x=0,y=0;
unsigned long long a,b;
long long fi(int n, int m) {
	long long num = 0;
	for (long long i = m; i <= n; i *= m) {
		num += n / i;
	}
	return num;
}
int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);
	cin >> N>>M;
	
	x = fi(N, 5) - fi(N - M, 5) - fi(M, 5);
	y = fi(N, 2) - fi(N - M, 2) - fi(M, 2);
	cout << min(x, y);
}