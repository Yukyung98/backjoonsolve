#include <iostream>
#include <string>

using namespace std;

int main()
{
	int n;
	int m;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> m;
		int* arr= new int[m];
		double sum = 0;
		double count = 0;
		double avg = 0;
		for (int j = 0; j < m; j++) {
			cin >> arr[j];
		}
		for (int k = 0; k < m; k++) {
			sum += arr[k];
		}
		avg = sum / m;
		for (int a = 0; a < m; a++){
			if (arr[a] > avg) {
				count++;
			}
		}
		cout << fixed;
		cout.precision(3);
		cout << count / m*100 << "%" << endl;
	}
}

