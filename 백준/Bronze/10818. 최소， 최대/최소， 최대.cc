#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;
    int* p;
    p = new int[N];
    for (int i = 0; i < N; i++) {
        cin >> p[i];
    }
    sort(p, p + N);
    cout << p[0] << " " << p[N - 1];
}