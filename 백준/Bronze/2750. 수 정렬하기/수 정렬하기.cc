#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int n;

int main()
{
	cin >> n;
	int* arr = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	int tmp;
	for (int i = 0; i < n; i++) {
		tmp = i;
		for (int j = i+1; j < n; j++) {
			if (arr[tmp] > arr[j]) {
				tmp = j;
			}
		}
		if (i != tmp) {
			swap(arr[tmp],arr[i]);
		}
	}
	for (int i = 0; i < n; i++) {
		cout << arr[i] << endl;
	}

}
