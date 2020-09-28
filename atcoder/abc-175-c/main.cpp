#include <bits/stdc++.h>

using namespace std;

int main()
{
    long long x, k, d;
    cin >> x >> k >> d;
    if(x < 0)
        x *= -1;
    long long factor = x/d;
        
    if(k >= factor){
        k-=factor;
        x -= factor*d;
        if(k % 2)
            x -= d;
    }
    else{
        x -= k*d;
    }
    cout << abs(x) << '\n';
    return 0;
}
