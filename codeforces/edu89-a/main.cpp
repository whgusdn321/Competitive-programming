#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T = 0;
    cin >> T;
    for(int tc=0; tc<T; tc++){
        int a, b;
        cin >> a >> b;
        int cnt = 0;
        if(a > b){
            // while(a != b && a && b){
            //     a -= 2;
            //     b -= 1;
            //     cnt++;
            // }
            int tmp = min(b, a-b);
            a -= tmp*2;
            b -= tmp;
            cnt += tmp;
        }
        else if( a < b){
            // while(a != b && a && b){
            //     a -= 1;
            //     b -= 2;
            //     cnt++;
            // }
            int tmp = min(b-a, a);
            a -= tmp;
            b -= tmp*2;
            cnt += tmp;
        }
        else{;}
        
        if(!a | !b){
            cout << cnt << '\n';
            continue;
        }
        else{ // a == b
            int tmp = 0;
            tmp = a/3;
            cnt += tmp*2;
            a %= 3;
            b %= 3;
        }
        int i=0;
        while(a>1 && b>1){
            if(i % 2){
                a -= 2;
                b -= 1;
            }
            else{
                a -= 1;
                b -= 2;
            }
            cnt++;
        }
        cout << cnt << '\n';
    }
    return 0;
}
