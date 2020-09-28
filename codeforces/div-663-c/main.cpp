#include <bits/stdc++.h>     

using namespace std;

long long MOD = 1e9+7;

long long fact(long long n){
    return (n==0) || (n==1) ? 1 : ((n%MOD)*(fact(n-1)%MOD))%MOD;
}
long long pow2(long long n){
    return (n==0) ? 1 : ((2%MOD)*(pow2(n-1)%MOD))%MOD;
}
int main()
{
    long long n;
    cin >> n;
    long long ans = (fact(n)%MOD - (pow2(n-1)%MOD))%MOD;
    if(ans >= 0){
        cout << ans << '\n';
    }
    else{
        cout << MOD + ans << '\n';
    }
    return 0;
}
