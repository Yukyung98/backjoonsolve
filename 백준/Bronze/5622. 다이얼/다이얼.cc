#include <iostream>
#include <string>

using namespace std;

int main()
{
	string str;
	cin >> str;	
	string alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	
	int sum = 0;
	for (int i = 0; i < str.length(); i++) {
		int loc = alp.find(str[i]);
		if (loc >= 0 && loc <= 2)
			sum += 3;
		else if (loc >= 3 && loc <= 5) {
			sum += 4;
		}
		else if (loc >= 6 && loc <= 8) {
			sum += 5;
		}
		else if (loc >= 9 && loc <= 11) {
			sum += 6;
		}
		else if (loc >= 12 && loc <= 14) {
			sum += 7;
		}
		else if (loc >= 15 && loc <= 18) {
			sum += 8;
		}
		else if (loc >= 19 && loc <= 21) {
			sum += 9;
		}
		else if(loc>=22 && loc<=25){
			sum += 10;
		}

	}
	cout << sum;

}

