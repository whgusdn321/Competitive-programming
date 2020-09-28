#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    int arr[1000000];
    cin >> n;
    map<int, int> dict;
    for(int i=0; i<n; i++){
        cin >>arr[i];
        dict[arr[i]] += 1;
    }
    int ans = 0;
    for(int i=0; i<n; i++){
        int num = arr[i];
        if(dict[num] >= 2){
            continue;
        }
        if(num != 1 && dict[1] > 0){
            continue;
        }
        else{
            bool found = false;
            for(int j=2; j*j <= num; j++){
                if(num % j == 0){
                    int factor1 = j;
                    int factor2 = num/j;
                    if(dict[factor1] || dict[factor2]){
                        found = true;
                        break;
                    }
                }
            }
            if(!found){
                ans++;
                //cout << num << '\n';
            }
        }
    }
    cout << ans << '\n';    
    return 0;
}
