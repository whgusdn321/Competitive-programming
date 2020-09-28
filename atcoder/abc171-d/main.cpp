#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    long long arr[100001];
    int q;
    int b, c;
    long long ans = 0;
    map<int, int> dict;
    cin >> n;
    for(int i=0; i<n; i++){
        cin >> arr[i];
        ans += arr[i];
        dict[arr[i]] += 1;
    }
    cin >> q;
    for(int i=0; i<q; i++){
        cin >> b >> c;
        //int before = dict[arr[b]];
        ans -= b * (long long)dict[b];
        ans += (long long)dict[b] * c;
        dict[c] += dict[b];
        dict[b] = 0;
        cout << ans << '\n';
    }
    return 0;
}