#include <iostream>
#include <string>

using namespace std;

int main()
{
	int i = 0;
	string str;
	while (true) {
		getline(cin, str);
		if (str == "")
			break;
		cout << str << endl;
	}

}

