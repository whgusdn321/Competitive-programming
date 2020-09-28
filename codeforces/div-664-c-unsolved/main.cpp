#include <bits/stdc++.h>

using namespace std;

bool inspect(vector<int> &vec, int num){
    for(int x:vec){
        if((x | num) == num)
            return true;
    }    
    return false;
}

int main()
{
    int n, m;
    int a[201];
    int b[201];
    cin >> n >> m;
    for(int i=0; i<n; i++){
        cin >> a[i];
    }
    for(int i=0; i<m; i++){
        cin >> b[i];
    }
    vector<vector<int>> cs(n, vector<int>());
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cs[i].push_back(a[i] & b[j]);
        }
    }
    int limit = 1<<9;
    int ans = 0;
    for(int num=0; num<limit; num++){
        bool poss = true;   
        for(int i=0; i<n; i++)
            poss &= inspect(cs[i], num);
            
        if(poss){
            ans = num;
            break;
        }
    }
    cout << ans << '\n';
    
    return 0;
}
