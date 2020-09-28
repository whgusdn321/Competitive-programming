#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> maap;

bool f(int a, int b){
    int cnt = 0;
    for(int i=a; i<a+2; i++){
        for(int j=b; j<b+2; j++){
            if(maap[i][j] == 1){
                cnt++;
            }
        }
    }
    if(cnt%2==0)
        return false;
    else
        return true;
}

// void make(int a, int b, int x, int y){
//     for(int i=a; i<a+2; i++){
//         for(int j=b; j<b+2; j++){
//             maap[i][j] = 1
//         }
//     }    
//     maap[x][y] = 0;
// }

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    int cnt = 0;
    cin >> n >> m;
    maap = vector<vector<int>>(n, vector<int>(m, 0));
    for(int i=0; i<n; i++){
        string tmp;
        cin >> tmp;
        for(int j=0; j<m; j++){
            maap[i][j] = tmp[j] -'0';
        }
    }
    
    if(n >= 4 && m >= 4){
        cout << -1 << '\n';
        return 0;
    }
    if(n < 2 || m < 2){
        cout << 0 << '\n';
        return 0;
    }
    if(n==2 && m==2){
        if(f(0, 0)){
            cout << 0 << '\n';
        }
        else{
            cout << 1 << '\n';
        }
        return 0;
    }
    if(n==2){
        for(int j=0; j<m-2; j++){
            if(!f(0, j)){
                cnt += 1;
            }
        }
        cout << cnt << '\n';
        return 0;
    }
    if(m==2){
        for(int i=0; i<n-2; i++){
            if(!f(i, 0)){
                cnt += 1;
            }
        }
        cout << cnt << '\n';
        return 0;
    }
    
    for(int i=0; i<n-1; i++){
        for(int j=0; j<m-2; j++){
            if( !(f(i, j) && f(i, j+1)) ){
                cnt += 1;
                for(int ii=i; ii<i+2; ii++){
                    for(int jj=j; jj<j+3; jj++){
                        maap[ii][jj] = 0;
                    }
                }
                maap[i+1][j+1] = 1;
            }
        }
    }
    cout << cnt << '\n';
    return 0;
}
