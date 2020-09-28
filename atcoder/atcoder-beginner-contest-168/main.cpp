#include <bits/stdc++.h>

using namespace std;

#define PI 3.14159265358979

int main(){
    double a, b, h, m;
    cin >> a >> b >> h >> m;
    cout.precision(10);
    int elapsed = 60*h + m;
    double hh = 0.5*elapsed;
    double mm = (6*elapsed)%360;
    double alpha = abs(hh-mm);
    if(alpha > 180)
        alpha -= 180;
    double c = sqrt(a*a + b*b - 2*a*b*(cos(alpha*PI/180.0)));
    // printf("%.10f", c);
    cout << fixed << c;
    
}