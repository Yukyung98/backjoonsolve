#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
#include<stack>

using namespace std;

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);
	int A, B, m;
	cin >> A >> B;
	cin >> m;
	int a=0;
	while (m--) {
		int x;
		cin >> x;
		a += pow(A, m)*x;
	}
	stack<int> res;
	int res2 = a;
	while (res2) {
		res.push(res2 % B);
		res2 /= B;
	}
	while (!res.empty()) {
		cout << res.top() << " ";
		res.pop();
	}
}