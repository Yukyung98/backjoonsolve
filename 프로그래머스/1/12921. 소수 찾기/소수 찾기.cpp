#include <vector>

using namespace std;

int solution(int n) {
    vector<bool> is_prime(n + 1, true); // 소수 여부를 저장하는 배열
    is_prime[0] = is_prime[1] = false; // 0과 1은 소수가 아님

    // 에라토스테네스의 체 알고리즘
    for (int i = 2; i * i <= n; ++i) {
        if (is_prime[i]) {
            for (int j = i * i; j <= n; j += i) {
                is_prime[j] = false; // 소수가 아닌 수를 표시
            }
        }
    }

    // 소수의 개수 세기
    int answer = 0;
    for (int i = 2; i <= n; ++i) {
        if (is_prime[i]) {
            ++answer;
        }
    }

    return answer;
}
