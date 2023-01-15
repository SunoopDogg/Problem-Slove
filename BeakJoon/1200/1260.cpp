#include <bits/stdc++.h>
using namespace std;

int arr[1001][1001];
int check1[1001];
int check2[1001];

void DFS(int start, int n) {
    cout << start << " ";
    check1[start] = 1;

    for (int i = 1; i <= n; i++)
        if (arr[start][i] && !check1[i]) DFS(i, n);
}

void BFS(int start, int n) {
    queue<int> q;

    q.push(start);
    check2[start] = 1;

    while (!q.empty()) {
        int cur = q.front();

        cout << cur << " ";
        q.pop();

        for (int i = 1; i <= n; i++)
            if (arr[cur][i] && !check2[i]) {
                check2[i] = 1;
                q.push(i);
            }
    }
}

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, v;
    cin >> n >> m >> v;

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        arr[a][b] = 1;
        arr[b][a] = 1;
    }

    DFS(v, n);
    cout << "\n";
    BFS(v, n);
}