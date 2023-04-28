#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	int n;
	
	cin >> n;
	double* arr = new double[n];
	int l = 0;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		l++;
	}	
	double max = *std::max_element(arr, arr+l);
	
	double sum = 0;
	for (int i = 0; i < n; i++) {
	
		arr[i]=(arr[i]/max) * 100;
		
		sum += arr[i];
	}
	double avg = 0;
	avg = sum / n;
	cout.precision(6);
	cout << avg<<endl;
}