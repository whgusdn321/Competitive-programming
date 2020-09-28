#include <bits/stdc++.h>

using namespace std;

int f(long long num){
    long long fact = 1;
    int lefts = 0;
    while(num/fact){
        lefts += (num % (fact*10))/fact;
        fact *= 10;
    }
    return lefts;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int tc;
    cin >> tc;
    for(int t=0; t<tc; t++){
        long long num;
        int s = 0;
        cin >> num >> s;
        
        long long cnt = 0;
        long long fact = 1;
        int lefts = f(num);
        
        
        while(lefts > s){
            if( (num%(fact*10)) / fact > 0){
                cnt += fact*(10 - (num%(fact*10)) / fact);
                num += fact*(10 - (num%(fact*10)) / fact);
                lefts = f(num);
            }
            fact *= 10;
        }
        
        cout << cnt << '\n';
    }
    return 0;
}