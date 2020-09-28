#include <bits/stdc++.h>

using namespace std;
map<int, int> dict;
bool cmp(int a, int b){
    return dict[a] > dict[b];
}

int main()
{   
    int tc;
    cin >> tc;
    for(int t=0; t<tc; t++){
        dict = map<int, int>();
        vector<int> vec;
        int n;
        cin >> n;
        for(int i=0; i<n; i++){
            int tmp;
            cin >> tmp;
            dict[tmp] += 1;
        }
        for(auto it=dict.begin(); it!= dict.end(); it++){
            vec.push_back(it->first);
        }
        sort(vec.begin(), vec.end(), cmp);
        for(int x : vec){
            cout << x << ' ';
        }
        cout << '\n';
        vector<int> ans;
        while(!vec.empty()){
            int cnt = 0;
            for(int i=0; i<vec.size(); i++){
                ans.push_back(vec[i]);
                dict[vec[i]] -= 1;
                if(dict[vec[i]] == 0){
                    cnt += 1;
                    // auto it = find(vec.begin(), vec.end(), vec[i]);
                    // vec.erase(it);
                    // vec.pop_back();
                }
            }
            for(int i=0; i<cnt; i++){
                vec.pop_back();
            }
        }
        for(int x : ans){
            cout << x << ' ';
        }
        cout << '\n';
        map<int, int> dict2;
        vector<int> ans2;
        for(int i=ans.size()-1; i>=0; i--){
            if(dict2[ans[i]] == 0){
                dict2[ans[i]] = i;
            }
            else{
                ans2.push_back(dict2[ans[i]] - i - 1); 
                dict2[ans[i]] = i;
            }
        }
        cout << *min_element(ans2.begin(), ans2.end()) << '\n';
        
    }
    
    return 0;
}

