#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
#include<stack>
#include<string>

using namespace std;

int DP[1000000];
int main() {
	ios_base::sync_with_stdio(NULL); cin.tie(0); cout.tie(0);
	int n;
	cin >> n;
	for (int i = 2; i <=n; i++) {
		DP[i] = DP[i - 1] + 1;
		if (i % 2 == 0) {
			DP[i] = min(DP[i], DP[i / 2] + 1);
		}
		if (i % 3 == 0) {
			DP[i] = min(DP[i], DP[i / 3] + 1);
		}
	}
	cout << DP[n];
	return 0;
}