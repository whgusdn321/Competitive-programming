#include <bits/stdc++.h>

using namespace std;

char arr[101][101];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int tc;
    cin >> tc;
    for(int t=0; t<tc; t++){
        int n, m;
        cin >> n >> m;
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                cin >> arr[i][j];
            }
        }
        int cnt = 0;
        for(int i=0; i<n-1; i++){
            if(arr[i][m-1] == 'R'){
                cnt += 1;
            }
        }
        for(int j=0; j<m-1; j++){
            if(arr[n-1][j] == 'D'){
                cnt += 1;
            }
        }
        cout << cnt << '\n';
    }
    return 0;
}
