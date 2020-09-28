#include <bits/stdc++.h>

using namespace std;

int arr[200001];
int n, k_;
int cnt = 0;
int first;

void ff(int start, int cnt, int k){
    // if(arr[start] % (cnt+1) == 0){
    //     arr[start] = arr[start] / (cnt+1);
    // }
    // else{
    //     arr[start] = arr[start] / (cnt+1) + 1;
    // }
    arr[start] = ceil(arr[start]/(double)(cnt+1));
    
    for(int i=start+1; i<n; i++){
        int needed = ceil(arr[i]/(double)arr[start]) - 1;
        arr[i] = ceil(arr[i] /((double)needed+1));
        k -= needed;
    }
    return;
}

bool f(int start, int cnt, int k){
    
    first = ceil(arr[start]/(double)(cnt+1));
    
    for(int i=start+1; i<n; i++){
        int needed = ceil(arr[i]/(double)first) - 1;
        k -= needed;
        if(k < 0)
            return false;
    }
    return true;
}

int main()
{
    cin >> n >> k_;
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }
    sort(arr, arr+n);
    
    if(k_ == 0){
        cout << arr[n-1] << '\n';
        return 0;
    }
    
    for(int idx=0; idx<n; idx++){
        if(idx == 4){
            cout << "nothing" << '\n';
        }
        int cnt = 0;
        int k = k_;
        bool poss = true;
        do{
            cnt++;
            k--;
            if(k < 0)
               break;
            poss = f(idx, cnt, k);
        }while(poss);
        
        if(cnt > 1){
            cout << "idx is : " << idx << " cnt is : " << cnt <<'\n';
            // arr[idx] =(int)ceil(arr[idx] /(double)(cnt)); 
            for(int i = 0; i<n; i++)
                cout << arr[i] << ' ';
            cout << '\n';
            ff(idx, cnt-1, k_);
            for(int i = 0; i<n; i++)
                cout << arr[i] << ' ';
            cout << '\n';
            cout << *max_element(arr, arr+n) << '\n';
            break;
        }
    }
    
    
    return 0;
}
