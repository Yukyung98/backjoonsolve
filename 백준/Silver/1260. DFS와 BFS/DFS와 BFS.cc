#include <iostream>
#include <queue>
using namespace std;
#define MAX 1001

int n, m, v; //정점개수, 간선개수, 시작정점
int map[MAX][MAX]; // 인접 행렬 그래프
bool visited[MAX]; // 정점 방문 여부
queue<int> q;

void reset() {
	for (int i = 1; i <= n; i++) {
		visited[i] = 0;
	}
}

void DFS(int v) {
	visited[v] = true;
	cout << v << " ";
	for (int i = 1; i <= n; i++) {
		if (map[v][i] == 1 && visited[i] == 0) {
			// 현재 정점과 연결되어 있고 방문되지 않았으면
			DFS(i);
		}
	}
}
void BFS(int v) {
	q.push(v);
	visited[v] = true; 
	cout << v << " ";
	while (!q.empty()) {
		v = q.front();
		q.pop();

		for (int w = 1; w <= n; w++) {
			if (map[v][w] == 1 && visited[w] == 0) {
				// 현재 정점과 연결되어있고 방문되지 않았으면
				q.push(w);
				visited[w] = true;
				cout << w << " ";
			}
		}
	}
}

int main() {
	cin >> n >> m >> v;
	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		map[a][b] = 1;
		map[b][a] = 1;
	}
	reset();
	DFS(v);
	cout << "\n";

	reset();
	BFS(v);
	return 0;
}