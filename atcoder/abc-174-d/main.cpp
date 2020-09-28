#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    string str;
    cin >> n;
    cin >> str;
    int left = 0, right = n-1;
    int cnt = 0;
    
    while(left <= right){
        while(left < n && str[left] != 'W')
            left++;
        while(right >= 0 && str[right] != 'R')
            right--;
        if(left < n && right >= 0 && left < right){
            char tmp = str[right];
            str[right] = str[left];
            str[left] = tmp;
            left++;
            right--;
            cnt++;
        }
            
    }
    cout << cnt << '\n';
    return 0;
}

