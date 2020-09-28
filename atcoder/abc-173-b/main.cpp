#include <bits/stdc++.h>

using namespace std;

int main(){
    
    int ac = 0, wa = 0, tle = 0, re = 0;
    int n = 0;
    cin >> n;
    while(n){
        string tmp;
        cin >> tmp;
        if(tmp == "AC")
            ac++;
        else if(tmp == "WA")
            wa++;
        else if(tmp == "TLE")
            tle++;
        else
            re++;
        n--;
    }
    cout <<"AC x " << ac << '\n' << "WA x " << wa << '\n' << "TLE x " << tle << '\n' << "RE x " << re << '\n';
    return 0;
}