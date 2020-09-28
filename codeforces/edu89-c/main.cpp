#include <bits/stdc++.h>

using namespace std;

int n, m;
int maap[30][30];
bool visited[30][30];

int bfs(){
    vector<vector<int>> vec(1, vector<int>());
    queue<vector<int>> qu;
    qu.push({0, 0, 0});
    int cnt = 0;
    while(!qu.empty()){
        vector<int> tmp = qu.front();
        qu.pop();
        int y = tmp[0];
        int x = tmp[1];
        int num = tmp[2];
        if(num == cnt){
            vec.back().push_back(maap[y][x]);
            if(y+1<n && !visited[y+1][x]){
                visited[y+1][x] = true;
                qu.push({y+1, x, num+1});
            }
            if(x+1<m && !visited[y][x+1]){
                visited[y][x+1] = true;
                qu.push({y, x+1, num+1});
            }
        }
        else{
            vec.push_back(vector<int>());
            cnt++;
            vec.back().push_back(maap[y][x]);
            if(y+1<n && !visited[y+1][x]){
                visited[y+1][x] = true;
                qu.push({y+1, x, num+1});
            }
            if(x+1<m && !visited[y][x+1]){
                visited[y][x+1] = true;
                qu.push({y, x+1, num+1});
            }
        }
        
    }
    // cout << "vector is : " << '\n';
    // for(vector<int> x : vec){
    //     for(int y : x){
    //         cout << y << ' ';
    //     }
    //     cout << '\n';
    // }
    int ans = 0;
    int l = 0, r = vec.size()-1;
    while(l <r){
        int one1= 0, zero1 =0, one2 = 0, zero2 = 0;
        for(int x : vec[l]){
            if(x == 0) 
                zero1++;
            else
                one1++;
        }
        
        for(int x : vec[r]){
            if(x == 0) 
                zero2++;
            else
                one2++;
           }
        
        ans += min(zero1+zero2, one1 + one2);
        l++;
        r--;
    }
    return ans;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T = 0;
    cin >> T;
    for(int tc=0; tc<T; tc++){
        cin >> n >> m;
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                cin >> maap[i][j];
            }
        }
        fill(visited[0], visited[0]+900, false);
        int ans = bfs();
        cout << ans << '\n';
    }
    return 0;
}
