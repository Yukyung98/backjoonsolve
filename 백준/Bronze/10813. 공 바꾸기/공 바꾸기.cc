#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	int n, m;
	cin >> n >> m;
	int* arr = new int[n+1];
	for (int i = 1; i < n+1; i++) {
		arr[i] = i;
	}
	int x, y;
	for (int j = 0; j < m; j++) {
		cin >> x>>y;
		swap(arr[x], arr[y]);
		
	}
	for (int k = 1; k < n+1; k++) {
		cout << arr[k] << " ";
	}
	
}