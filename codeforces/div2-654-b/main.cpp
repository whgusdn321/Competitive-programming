#include <bits/stdc++.h>

using namespace std;

long long sum(long long a, long long b){
    long long n = (b - a)+1;
    return ((a + b)/2.0)*n;
}

int main()
{
    int tc;
    cin >> tc;
    for(int i=0; i<tc; i++){
        long long n, r;
        cin >> n >> r;
        if(n == 1 || r == 1)
            cout << 1 << '\n';
        else if(n > r){
            cout << sum(1, r) << '\n';   
        }
        else{// n <= r
            cout << sum(1, n-1) + 1 << '\n';
        }
    }
    return 0;
}
