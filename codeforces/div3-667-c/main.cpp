#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int tc;
    cin >> tc;
    for(int t=0; t<tc; t++){
        int n, x, y;
        cin >> n >> x >> y;
        int k = y-x;
        for(int i=k; i>=1; i--){
            if(k%i == 0){
                int hop = k/i;
                if(1 + k/hop <= n){
                    // cout << "hop is " << hop << " k is : " << k << " i is : " << i << '\n';
                    vector<int> ans;
                    int cnt = 0;
                    for(int j=x; j<=y; j+=hop){
                        cnt++;
                        ans.push_back(j);
                        if(cnt >= n)
                            break;
                    }
                    x -= hop;
                    while(x > 0 && cnt < n){
                        cnt++;
                        ans.push_back(x);
                        x -= hop;
                    }
                    while(cnt < n){
                        cnt++;
                        y += hop;
                        ans.push_back(y);
                    }
                    for(int x: ans)
                        cout << x << ' ';
                    cout << '\n';
                    break;
                    
                }
            }
        }
    }
    return 0;
}