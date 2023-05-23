#include <iostream>
#include <string>
#include <vector>

using namespace std;

int a, b, c, d, e,f;
double x, y;
int main()
{
	cin >> a >> b >> c >> d >> e >> f;
	for (int i = -999; i<= 999; i++) {
		for (int j = -999; j <= 999; j++) {
			if ((i * a + j * b == c) && (i * d + j * e == f)) {
				cout << i << " " << j;
			}
		}
	}
	
}

