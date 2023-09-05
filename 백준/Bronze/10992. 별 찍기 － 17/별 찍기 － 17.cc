#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>
#include <string>

using namespace std; 
long long n;
string line;


int main() {
	cin >> n;
	for (int i = 1; i <= n; ++i) {
		int cnt = 0;
		if (i == n) {
			for (int j = 0; j < n * 2 - 1; j++)
				cout << "*";
			
		}else{
		for (int j = 0; j < n - i; j++)
			cout << " ";
		cout << "*";
		
		while (i > 1) {
			for (int j = 0; j < (i*2+1)-4; j++)
				cout << " ";
			cout << "*";
			break;
		}
		cout << endl;
	}
	}
}
