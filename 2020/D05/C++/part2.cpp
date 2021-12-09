#include <bits/stdc++.h>
using namespace std;
#define ll int64_t

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    freopen("../input.in","r",stdin);
    freopen("../part2.out","w",stdout);
    vector<int> v;
    string s;
    while (cin >> s) {
        int l = 0, r = 128;
        for (int i = 0; i < 7; i++) {
            if (s[i] == 'F') r = (l+r)/2;
            if (s[i] == 'B') l = (l+r)/2;
        }
        int l2 = 0, r2 = 8;
        for (int i = 7; i < 10; i++) {
            if (s[i] == 'L') r2 = (l2+r2)/2;
            if (s[i] == 'R') l2 = (l2+r2)/2;
        }
        int x = (l+r)/2;
        int y = (l2+r2)/2;
        v.push_back(x*8+y);
    }
    sort(v.begin(),v.end());
    for (int i = 1; i < v.size(); i++) {
        if (v[i] == v[i-1]+2) cout << v[i]-1 << "\n";
    }
}
