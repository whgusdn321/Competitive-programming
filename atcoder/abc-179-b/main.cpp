#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int a, b;
    int t = 0;
    for(int i=0; i<n; i++){
        cin >> a >> b;
        if(a==b){
            t++;
            if(t==3){
                cout << "Yes" << '\n';
                return 0;
            }
        }
        else{
            t = 0;
        }
        
    }
    cout << "No" << '\n';
    return 0;
}
