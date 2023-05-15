#include <iostream>
#include <string>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int num;
		string s;
		cin >> num;
		cin >> s;
		for (int j = 0; j < s.length(); j++) {
			for (int k = 0; k <num; k++) {
				cout << s[j];
			}
		}
		cout << endl;
	}
	return 0;

}

