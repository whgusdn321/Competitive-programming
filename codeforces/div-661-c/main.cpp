#include <bits/stdc++.h>

using namespace std;

int main(){
    int tc;
    cin >> tc;
    int arr[100];
    for(int t=0; t<tc; t++){
        int n;
        cin >> n;
        if(n == 1){
            cin >> arr[0];
            cout << 0 << '\n';
            continue;
        }
        for(int i=0; i<n; i++){
            cin >> arr[i];
        }
        map<int, vector<int>> dict;
        map<int, int> dict2;
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                int weight = arr[i] + arr[j];
                if(find(dict[weight].begin(), dict[weight].end(), i) == dict[weight].end() 
                && find(dict[weight].begin(), dict[weight].end(), j) == dict[weight].end()){
                    dict[weight].push_back(i);
                    dict[weight].push_back(j);
                    dict2[weight] += 1;
                }
            }    
        }
        // cout << "hello" << '\n';
        vector<int> tmp;
        for(auto it=dict2.begin(); it!=dict2.end(); it++){
            tmp.push_back(it->second);
        }
        cout << *max_element(tmp.begin(), tmp.end()) << '\n';
        
    }
}