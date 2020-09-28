#include <bits/stdc++.h>

using namespace std;

int main()
{
    double c;
    cin >> c;
    double l, r;
    l = 1;
    r = 1e10;
    //double mid = (l+r)/
    cout.precision(7);
    while(r-l >= 1e-6){
        double mid = (l+r)/2;   
        if(mid*mid + sqrt(mid) > c){
            r = mid;
        }
        else{
            l = mid;
        }
    }
    cout << r << '\n';
    return 0;
}
