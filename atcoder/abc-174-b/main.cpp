#include <bits/stdc++.h>

using namespace std;

int main()
{
    long long n, d;
    long long x, y;
    int points = 0;
    cin >> n >> d;
    for(int i=0; i<n; i++){
        cin >> x >> y;
        if(x*x + y*y <= d*d)
            points += 1;
        else
            continue;
    }
    cout << points << '\n';
    return 0;
}
