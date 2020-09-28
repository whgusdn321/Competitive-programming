#include <bits/stdc++.h>

using namespace std;

int main()
{
    int tc;
    int n;
    cin >> tc;
    for(int t=0; t<tc; t++){
        cin >> n;
        map<int, int> dict;
        for(int i=0; i<n; i++){
            int tmp;
            cin >> tmp;
            dict[tmp] += 1;
        }
        if(dict.size() == 1){
            cout << "YES" << '\n';
        }
        else{
            vector<int> vec;
            for(auto it=dict.begin(); it!=dict.end(); it++){
                vec.push_back(it->first);
            }
            sort(vec.begin(), vec.end());
            bool found = true;
            for(int i=0; i<vec.size()-1; i++){
                if(vec[i]-vec[i+1] != -1){
                    found = false;
                    break;
                }
            }
            if(found)
                cout << "YES" << '\n';
            else
                cout << "NO" << '\n';
        }
    }
    return 0;
}

