#include <bits/stdc++.h>
using ll = long long;
using namespace std;
using boss = pair<ll, ll>;

ll calculateTime(ll hp, ll dps) {
    ll timeTaken = hp / dps;
    if (hp % dps != 0) timeTaken += 1;
    return timeTaken;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    cin >> n >> m >> k;

    vector<ll> dpsData(n);
    for (ll& i : dpsData) cin >> i;

    vector<boss> bossData(k);
    for (auto& [bossHp, bossReward] : bossData) cin >> bossHp >> bossReward;

    vector<ll> charReward(n, 0);
    const int bitEnd = 1 << k;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < bitEnd; ++j) {
            ll charTimeTaken = 0;
            ll reward = 0;
            for (int l = 0; l < k; ++l) {
                if ((j & (1 << l)) == 0) continue;

                auto [bossHp, bossReward] = bossData[l];
                ll timeTaken = calculateTime(bossHp, dpsData[i]);

                charTimeTaken += timeTaken;
                reward += bossReward;
            }

            if (charTimeTaken > 900) continue;
            charReward[i] = max(charReward[i], reward);
        }
    }

    sort(charReward.begin(), charReward.end(), greater<ll>());

    ll result = 0;
    for (int i = 0; i < m; ++i) result += charReward[i];

    cout << result;

    return 0;
}