#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    long long sum = 0;
    for(int a=1; a<=n; a++){
        for(int b=1; b<=n; b++){
            if(a*b < n){
                sum++;
            }
            else{
                break;
            }
        }
    }
    cout << sum << '\n';
    return 0;
}
