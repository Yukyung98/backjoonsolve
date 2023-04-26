#include <iostream>
using namespace std;

int main() {
    int *p;
    int arr_size;
    int k;
    int c = 0;
    cin >> arr_size;
    p = new int[arr_size];
    for (int i = 0; i < arr_size; i++) {
        cin >> p[i];
    }
    cin >> k;
    for (int j = 0; j < arr_size; j++) {
        if (p[j] == k) {
            c++;
        }
    }
    cout << c;
    delete[] p;
}