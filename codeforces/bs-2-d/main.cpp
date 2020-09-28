#include <bits/stdc++.h>

using namespace std;

int m, n;
vector<vector<int>> people;

bool f(int hour){
    int num = 0;
    for(vector<int> tmp : people){
        int t, y, z, x;
        t = tmp[0];
        z = tmp[1];
        y = tmp[2];
        x = (hour/(y+z*t))*z + min(hour%(y+z*t), z*t)/t;
        num += x;
    }
    return (num >= m);
}
int main()
{
    cin >> m >> n;
    for(int i=0; i<n; i++){
        int t, z, y;
        cin >> t >> z >> y;
        people.push_back({t, z, y});
    }
    int l = 0;
    int r = people[0][0]*m + m/people[0][1]*people[0][2];
    while(l < r-1){
        int mid = (l+r)/2;
        if(f(mid)){
            r = mid;
        }
        else{
            l = mid;
        }
    }
    cout << r << '\n';
    int sum = 0;
    for(int i=0; i<n; i++){
        auto tmp = people[i];
        int t, y, z, x;
        t = tmp[0];
        z = tmp[1];
        y = tmp[2];
        x = (r/(y+z*t))*z + min(r%(y+z*t), z*t)/t;
        if(m - sum >= x){
            cout << x << ' ';
            sum += x;
        }
        else{
            cout << m - sum << ' ';
            sum = m;
        }
    }
    return 0;
}
