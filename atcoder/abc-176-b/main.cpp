#include <bits/stdc++.h>

using namespace std;

int main()
{
    string n;
    cin >> n;
    int sum = 0;
    for(char ch : n){
        int num = ch - '0';
        sum += num;
    }
    if(sum % 9 == 0)
        cout << "Yes" << '\n';
    else
        cout << "No" << '\n';
    return 0;
}
