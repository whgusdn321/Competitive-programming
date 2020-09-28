#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int a = n%1000;
    if(a)
        cout << 1000-a << '\n';
    else
        cout << 0 << '\n';
    return 0;
}
