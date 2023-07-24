#include<iostream>
#include<vector>
#include<algorithm>
#define INF 1000000000
using namespace std;
long long T, N, M;
long long x, y, c;
long long B;

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);
	char apl[26] = { 'A','B','C','D','E','F','G','H','I',
		'J','K','L','M','N','O','P','Q','R','S','T','U',
		'V','W','X','Y','Z'
	};
	cin >> T >> B;
	char arr[27] ;
	int d = T % B;
	int c = T / B;
	int pos = 0;
	while (1) {
		if (c == 0) {
			if (d > 9) {
				arr[pos] = apl[d - 10];
				break;
			}
			arr[pos] = (char)(d+48);
			break;
		}
		if (d > 9) {
			arr[pos] = apl[d-10];
		}
		else {
			arr[pos] = (char)(d + 48);
			
		}
		pos++;
		d = c % B;
		c = c / B;
	}

	for (int i = pos; i >= 0; i--) {
		cout << arr[i] ;
	}
}