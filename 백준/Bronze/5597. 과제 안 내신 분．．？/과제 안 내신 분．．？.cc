#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	int arr[31] = { 0, };
	int n;
	for (int i = 0; i <28; i++) {
		cin >> n;
		arr[n] = 1;
	}
	for (int j = 1; j <= 30; j++) {
		if (arr[j] == 0) {
			cout << j << endl;
		}
	}

}