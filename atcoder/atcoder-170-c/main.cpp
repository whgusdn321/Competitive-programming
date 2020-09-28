#include <bits/stdc++.h>

using namespace std;

int main()
{
    bool arr[102];
    fill(arr, arr+102, false);
    int x, n;
    cin >> x >> n;
    int tmp;
    for(int i=0; i<n; i++){
        cin >> tmp;
        arr[tmp] = true;
    }
    int i = x;
    int j = x;
    while(arr[i]){
        i--;
    }
    while(arr[j]){
        j++;
    }
    if(i == j){
        cout << i << '\n';
    }
    else{
        if(x - i == j - x){
            cout << i << '\n';
        }
        else if( x - i < j - x){
            cout << i << '\n';
        }
        else{
            cout << j << '\n';
        }
    }
    
    return 0;
}
