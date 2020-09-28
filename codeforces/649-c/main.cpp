#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    vector<int> ans;
    int n;
    int a[100001];
    cin >> n;
    for(int i=0; i<n; i++){
        cin >> a[i];
    }
    int last = 0;
    int i = 0;
    int j = -1;
    queue<int> qu;
    // cout << "qu.size() is : " << qu.size() << '\n';
    while(i < n){
        while(qu.empty()){// fill in queue...
            j = j+1;
            if(j < n){
                for(int x = last; x<a[j]; x++){
                    qu.push(x);
                }
                last = a[j];
            }
        }
        if(j == n-1 && qu.size() == 1 && qu.front() == a[i]){
            qu.push(++last); // avoid buffer underflow
        }
        
        if(qu.front() == a[i]){
            int tmp = qu.front();
            qu.pop();
            qu.push(tmp);
        }
        ans.push_back(qu.front());
        qu.pop();
        i++;
    }
    // while(!qu.empty()){
    //     cout << "qu : " << ' ';
    //     cout <<qu.front() << ' ';
    //     cout << "qu.size() is : " << qu.size() << '\n';
    //     // qu.pop();
    // }
    if(qu.empty()){
        for(int x : ans)
            cout << x << ' ';
    }
    else{
        cout << -1;
    }
    return 0;
}
