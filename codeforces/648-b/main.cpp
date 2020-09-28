#include <bits/stdc++.h>

using namespace std;

int a[555];
int b[555];

void exchage(int i, int j){
    int temp = a[i];
    a[i] = a[j];
    a[j] = temp;
    temp = b[i];
    b[i] = b[j];
    b[j] = temp;
    return;
}

void solve(){
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        cin >> a[i];
    }
    for(int i=0; i<n; i++){
        cin >> b[i];
    }
    //for(int i=0; i<n; i++){
    //    int min_idx = i; 
    //    int min_val = a[i];
    //    for(int j=i; j<n; j++){
    //        if(a[j] < min_val){
    //            min_idx = j;
    //            min_val = a[j];
    //        }
    //    }
    //    if(min_idx == i)
    //        continue;
    //    else if(b[min_idx] != b[i])
    //        exchange(i, min_idx);
    //    else{
    //        bool found = false;
    //        for(int l=i+1; l<n; l++){
    //            if(l != min_idx && b[i] != b[l]){
    //                exchage(i, l);
    //                exchage(min_idx, i);
    //                found = true;
    //                break;
    //            }
    //        }
    //        if(!found){
    //            cout << "No" << '\n';
    //            return;
    //        }
    //    }
    //}
    //cout << "Yes" << '\n';
    if(is_sorted(a, a+n))
        cout << "Yes" << '\n';
    else{
        int found1 = 0, found2 = 1;
        for(int i = 0; i<n; i++){
            found1 += b[i];
            found2 *= b[i];
        }
        if(found1 == 0 || found2 == 1)
            cout << "No" << '\n';
        else 
            cout << "Yes" << '\n';
    }
    
    return;
        
}

int main()
{
    int tc;
    cin>>tc;
    while(tc>0){
        solve();
        tc--;
    }
    return 0;
}
