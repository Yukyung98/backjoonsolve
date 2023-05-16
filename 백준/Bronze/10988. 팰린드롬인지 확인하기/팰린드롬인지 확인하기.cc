#include <iostream>
#include <string>

using namespace std;

int main()
{
	string s;
	cin >> s;
	int len = s.length();
	int total2 = len / 2;
	int count = 0;
	int k = len - 1;
	for (int i = 0; i < total2 ; i++) {
		if (s[i] == s[k]) {
			count++;
		}
		k--;
	}
	if (count == total2) {
		cout << "1";
	}
	else {
		cout << "0";
	}
	
}

