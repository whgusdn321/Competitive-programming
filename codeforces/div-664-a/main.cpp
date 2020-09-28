#include <bits/stdc++.h>

using namespace std;

int main()
{
    int tc;
    cin >> tc;
    for(int t=0; t<tc; t++){
        int r, g, b, w;
        cin >> r >> g >> b >> w;
        int odd = 0, even = 0;
        bool found = false;
        if(r%2)
            odd+=1;
        else
            even+=1;
        if(g%2)
            odd+=1;
        else
            even+=1;
        if(b%2)
            odd+=1;
        else
            even+=1;
        if(w%2)
            odd+=1;
        else
            even+=1;   
            
        if(odd < 2)
            found = true; 
            
        if(r && g && b)
            if(even < 2)
                found = true;
        if(found)
            cout << "YES" << '\n';
        else
            cout << "NO" << '\n';
    }
    return 0;
}
