#include <bits/stdc++.h>

using namespace std;

#define MAX 1000000000000000000

int main()
{
    int n;
    cin >> n;
    long long temp;
    long long a = 1;
    for(int i=0; i<n; i++){
        cin >> temp;
        if(temp == 0){
            a = 0;
            break;
        }
        else if(a <= MAX/temp)
            a *= temp;
        else{
            a = -1;
            for(int j = i; j<n; j++){
                cin >> temp;
                if(temp == 0)
                    a = 0;
            }
            break;
        }
    }
    cout << a;
    return 0;
}
