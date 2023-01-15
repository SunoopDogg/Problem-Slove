#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> v(27);

void preorder(int n) {
    char result = 'A' + n;

    cout << result;
    if (v[n][0] != -1) preorder(v[n][0]);
    if (v[n][1] != -1) preorder(v[n][1]);
}

void inorder(int n) {
    char result = 'A' + n;

    if (v[n][0] != -1) inorder(v[n][0]);
    cout << result;
    if (v[n][1] != -1) inorder(v[n][1]);
}

void postorder(int n) {
    char result = 'A' + n;

    if (v[n][0] != -1) postorder(v[n][0]);
    if (v[n][1] != -1) postorder(v[n][1]);
    cout << result;
}

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        char X, A, B;
        cin >> X >> A >> B;
        if (A != '.')
            v[X - 'A'].push_back(A - 'A');
        else
            v[X - 'A'].push_back(-1);
        if (B != '.')
            v[X - 'A'].push_back(B - 'A');
        else
            v[X - 'A'].push_back(-1);
    }

    preorder(0);
    cout << "\n";
    inorder(0);
    cout << "\n";
    postorder(0);
}