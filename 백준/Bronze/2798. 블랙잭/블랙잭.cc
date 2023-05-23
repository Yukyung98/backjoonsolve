#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int n; int m;
	cin >> n >> m;
	int* arr = new int[n];
	int sum = 0;
	int min= 100000;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	int t = 0;
	for (int i = 0; i < n-2; i++) {
		for (int j = i+1; j < n-1; j++) {
			for (int k = j+1; k < n; k++) {
				sum = arr[i] + arr[j] + arr[k];
				if (m - sum >= 0 && m-sum <=min) {
					min = m - sum;
					t = sum;
				}
			}
		}
	}
	cout << t;
}

