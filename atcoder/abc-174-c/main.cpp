#include <bits/stdc++.h>

using namespace std;

int main()
{
    int k;
    cin >> k;
    int tmp = 7, cnt = 1;
    map<int, bool> dict;
    while(tmp%k != 0 && dict[tmp%k] == false){
        //prepare for next
        //cout << "tmp is : " << tmp << '\n';
        tmp %= k;
        dict[tmp] = true;
        tmp = 10*tmp + 7;
        cnt++;
    }
    if(tmp%k==0)
        cout << cnt << '\n';
    else
        cout << -1 << '\n';
    return 0;
}
