#include <bits/stdc++.h>

using namespace std;

int main()
{
    int tc;
    cin >> tc;
    for(int t=0; t<tc; t++){
        string s;
        cin >> s;
        int n = s.size();
        priority_queue<int> pq;
        int cnt = 0;
        for(int i=0; i<n; i++){
            if(s[i] == '1'){
                cnt++;
                if(i==n-1){
                    pq.push(cnt);
                }
                    
            }
            else{
                if(cnt){
                    pq.push(cnt);
                    cnt = 0;
                }
                else
                    cnt = 0;
            }
        }
        
        int ans = 0;
        int i = 0;
        while(!pq.empty()){
            int tmp = pq.top();
            pq.pop();
            if(i % 2 == 0)
                ans += tmp;
            i++;
        }
        cout << ans << '\n';
    }
    return 0;
}
