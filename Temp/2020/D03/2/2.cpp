#include <bits/stdc++.h>
using namespace std;
#define ll int64_t

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    vector<string> v;
    int x, y;
    string s;
    while (cin >> s) {
        s = s+s; s = s+s;
        s = s+s; s = s+s;
        s = s+s; s = s+s;
        s = s+s;
        x = s.size();
        v.push_back(s);
    }
    y = v.size();
    int i = 0, q = 0, count = 0;
    while (i < y && q < x) {
        if (v[i][q] == '#') {
            count++;
        }
        i+=1; q+=1;
    }
    int ans = count;
    i = 0; q = 0; count = 0;
    while (i < y && q < x) {
        if (v[i][q] == '#') {
            count++;
        }
        i+=1; q+=3;
    }
    ans *= count;
    i = 0; q = 0; count = 0;
    while (i < y && q < x) {
        if (v[i][q] == '#') {
            count++;
        }
        i+=1; q+=5;
    }
    ans *= count;
    i = 0; q = 0; count = 0;
    while (i < y && q < x) {
        if (v[i][q] == '#') {
            count++;
        }
        i+=1; q+=7;
    }
    ans *= count;
    i = 0; q = 0; count = 0;
    while (i < y && q < x) {
        if (v[i][q] == '#') {
            count++;
        }
        i+=2; q+=1;
    }
    ans *= count;
    cout << ans << "\n";
}