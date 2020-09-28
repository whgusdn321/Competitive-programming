#include <bits/stdc++.h>

using namespace std;
int n;
bool f(long long x, int w, int h){
    //cout << "(x/w)*(x/h) is : " << (x/w)*(x/h) <<'\n';
    if((x/w) * (x/h) >= n ){
        //cout << "(x/w)*(x/h) is : " << (x/w)*(x/h) <<'\n';
        return true;
    }
    else{
        return false;
    }
}

int main()
{
    long long w, h;
    cin >> w >> h >> n;
    long long l = 0, r = max(w, h)*(sqrt(n)+1);
    while(l < r-1){
        long long m = (l+r)/2;
        //cout << "m is " <<m << " r is " << r <<" l is : " << l << '\n';
        if(f(m, w, h))
            r = m;
        else
            l = m;
    }
    cout << r << '\n';
    return 0;
}
