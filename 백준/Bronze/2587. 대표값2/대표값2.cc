#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int n=5;
int sum, avg;
int main()
{
	int min = 0;
	int arr[5] = {0,};
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		sum += arr[i];
	}
	avg = sum / 5;
	for (int i = 0; i < 5; i++) {
		min = i;
		for (int j = i; j < 5; j++) {
			if (arr[min] > arr[j]) {
				min = j;
			}
		}
		if (min != i) {
			swap(arr[min], arr[i]);
		}
	}
	cout << avg << endl;
	cout << arr[2];


}
