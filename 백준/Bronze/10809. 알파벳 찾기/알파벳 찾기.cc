#include <iostream>
#include <string>
using namespace std;

int main()
{
	string avr;
	string alp = "abcdefghijklmnopqrstuvwxyz";
	cin >> avr;
	for (int i = 0; i < alp.length(); i++) 
		cout << (int)avr.find(alp[i]) << " ";
	
	return 0;

}
