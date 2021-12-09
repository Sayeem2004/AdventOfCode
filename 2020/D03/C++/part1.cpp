#include <bits/stdc++.h>
using namespace std;
#define ll int64_t

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    freopen("../input.in","r",stdin);
    freopen("../part1.out","w",stdout);
    vector<string> v;
    int x, y;
    string s;
    while (cin >> s) {
        s = s+s; s = s+s; s = s+s; s = s+s; s = s+s; s = s+s; s = s+s;
        x = s.size();
        v.push_back(s);
    }
    y = v.size();
    int i = 0, q = 0, count = 0;
    while (i < y && q < x) {
        if (v[i][q] == '#') {
            count++;
        }
        i+=1; q+=3;
    }
    cout << count << "\n";
}
