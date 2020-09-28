#include <bits/stdc++.h>

using namespace std;

bool cmp(const pair<int, int> &a1, const pair<int, int> &a2){
    return (a1.second > a2.second);
}

int main()
{   
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int h, w, m;
    cin >> h >> w >> m;
    unordered_map<int, int> dict1, dict2;
    map<pair<int, int>, bool> dict3;
    for(int i=0; i<m; i++){
        cin >> h >> w;
        dict1[h] += 1;
        dict2[w] += 1;
        dict3[{h, w}] = true;
    }
    vector<pair<int, int>> vec1, vec2;
    for(auto it = dict1.begin(); it!=dict1.end(); it++){
        vec1.push_back({it->first, it->second});
    }
    
    for(auto it = dict2.begin(); it!=dict2.end(); it++){
        vec2.push_back({it->first, it->second});
    }
    sort(vec1.begin(), vec1.end(), cmp);
    sort(vec2.begin(), vec2.end(), cmp);
    int ans = vec1[0].second + vec2[0].second;
    unordered_map<int, bool> dict11, dict22;
    
    for(int i=0; i<vec1.size(); i++){
        if(vec1[i].second == vec1[0].second){
            dict11[vec1[i].first] = true;
        }
        else{
            break;
        }
    }
    for(int i=0; i<vec2.size(); i++){
        if(vec2[i].second == vec2[0].second){
            dict22[vec2[i].first] = true;
        }
        else{
            break;
        }
    }
    int combis = dict11.size() * dict22.size();
    for(auto it=dict3.begin(); it!=dict3.end(); it++){
        int hh = (it->first).first;
        int ww = (it->first).second;
        if(dict11[hh] && dict22[ww]){
            combis --;
        }
        else{
            continue;
        }    
    }
    if(combis==0)
        cout << ans - 1 << '\n';
    else
        cout << ans << '\n';
    
    return 0;
}
