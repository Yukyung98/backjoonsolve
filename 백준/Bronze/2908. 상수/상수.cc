#include <iostream>
#include <string>
#include<algorithm> 
using namespace std;

int main()
{
	string s1;
	string s2;
	cin >> s1;
	cin >> s2;
	reverse(s1.begin(), s1.end());
	reverse(s2.begin(), s2.end());
	int num1 = stoi(s1);
	int num2 = stoi(s2);
	
	cout << max(num1, num2);
}

