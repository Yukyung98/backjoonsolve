#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
#include<stack>
#include<string>

using namespace std;

char map[65][65];

void qt(int y, int x, int n) {
	if (n == 1) {
		cout << map[y][x];
		return;
	}
	for (int i = y; i < y + n; i++) {
		for (int j = x; j < x + n; j++) {
			if (map[y][x] != map[i][j]) {
				cout << '(';
				qt(y, x, n / 2);
				qt(y, x + n / 2, n / 2);
				qt(y + n / 2, x, n / 2);
				qt(y + n / 2, x + n / 2, n / 2);
				cout << ')';
				return;
			}
		}
	}
	cout << map[y][x];
	return;
}
int main() {
	ios_base::sync_with_stdio(NULL); cin.tie(0); cout.tie(0);
	int N;
	string s;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> s;
		for (int j = 0; j < N; j++) {
			map[i][j] = s[j];
		}
	}
	qt(0, 0, N);

}