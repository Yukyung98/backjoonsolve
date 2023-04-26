#include <iostream>
using namespace std;

int main() {
    int N, x;
    cin >> N>>x;
    int* p;
    p = new int[N];
    for (int i = 0; i < N; i++) {
        cin >> p[i];
    }
    for (int j = 0; j < N; j++) {
        if (p[j] < x) {
            cout << p[j]<< " ";
        }
    }
}