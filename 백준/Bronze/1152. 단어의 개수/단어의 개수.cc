#include <iostream>
#include <string>
using namespace std;

int main()
{
	string s1;
	getline(cin, s1);
	int count = 1;
	for (int i = 0; i < s1.length(); i++) {
		if (s1[i] == ' ') {
			count++;
		}
	}
	if (s1[0] == ' ') {
		count--;
	}
	if (s1[s1.length() - 1] == ' ') {
		count--;
	}
	cout << count; 
}

