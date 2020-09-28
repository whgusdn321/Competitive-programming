#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int tc;
    cin >> tc;
    for(int t=0; t<tc; t++){
        int a, b, x, y, n;
        cin >> a >> b >> x >> y >> n;
        int n_ = n, a_ = a, b_ = b;
        long long res1, res2;
        if(a-n < x){
            n -= (a - x);
            a = x;
            if(n>0)
                b = max(y, b - n);
        }
        else{
            a -= n;
            n = 0;
            b = b;
        }
        res1 = (long long)a*b;
        
        if(b_- n_ < y){
            n_ -= (b_ - y);
            b_ = y;
            if(n_>0)
                a_ = max(x, a_ - n_);
            
        }
        else{
            b_ -= n_;
            n_ = 0;
            a_ = a_;
            
        }
        res2 = (long long)a_*b_;
        
        cout << min(res1, res2) << '\n';
    }
    return 0;
}
