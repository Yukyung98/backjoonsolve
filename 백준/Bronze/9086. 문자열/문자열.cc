#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main() {
	int n;
	cin >> n;
	string str;
	for (int i = 1; i <= n; i++) {
		cin >> str;
		cout << str[0] << str[str.size() - 1] << '\n';
	}
}
