#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, m, sy, sx;
    cin >> n >> m >> sy >> sx;
    int total_cnt = 0;
    if(sx < 0)
        sx += m;
    while(total_cnt < n*m){
        int row_cnt = 0;
        while(row_cnt < m){
            if(row_cnt != 0)
                sx = sx+1;
            if(sx > m)
                sx -= m;
            cout << sy << ' ' << sx << '\n';
            row_cnt += 1;
            total_cnt += 1;
        }
        sy = (sy+1);
        if(sy > n)
            sy -= n;
    }
    return 0;
}
