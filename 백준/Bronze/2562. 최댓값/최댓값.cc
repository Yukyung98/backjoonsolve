#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int val[9];
    for (int i = 0; i < 9; i++) {
        cin >> val[i];
    }
    int max = 0;
    int index;
    for (int i = 0; i < 9; i++) {
        if (val[i] > max) {
            index = i+1;
            max = val[i];
        }
    }
    cout << max << endl << index;
}