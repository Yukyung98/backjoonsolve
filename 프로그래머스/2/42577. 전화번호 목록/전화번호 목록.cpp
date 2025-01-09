#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;

bool solution(vector<string> phone_book) {
    unordered_map<string, int> book;
    for (string i : phone_book) {
        book[i] = 1;
    }
    for (string i : phone_book) {
        string tmp = "";
        for (char c : i) {
            tmp += c;
            if (book.find(tmp) != book.end() && tmp != i) {
                return false; // 접두사가 존재
            }
        }
    }

    return true; // 접두사가 없는 경우
}
