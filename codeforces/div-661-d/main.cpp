#include <bits/stdc++.h>
 
using namespace std;
 
int main()
{
    int tc;
    cin >> tc;
    for(int t=0; t<tc; t++){
        int n;
        string s;
        cin >> n;
        cin >> s;
        vector<vector<int>> vec1, vec2;
        vector<int> idx1, idx2;
        int cnt = 0;
        vector<int> answer(n, 0);
        for(int i=0; i<n; i++){
            char cnum = s[i];
            if(cnum == '0'){
                if(vec2.empty()){
                    //push new string"0" to vec1
                    cnt += 1;
                    vec1.push_back({cnt});
                    answer[i] = cnt;  // vec1.size() + vec2.size();
                }
                else{
                    //vector<int> tmp = vec2.back();
                    answer[i] = vec2.back()[0];
                    vec1.push_back(vec2.back());
                    vec2.pop_back();
                }
            }
            else{ // cnum == 1
                if(vec1.empty()){
                    //push new
                    cnt += 1;
                    vec2.push_back({cnt});
                    answer[i] = cnt; //vec1.size() + vec2.size();
                }
                else{
                    //vector<int> tmp = vec1.back();
                    answer[i] = vec1.back()[0];
                    vec2.push_back(vec1.back());
                    vec1.pop_back();
                }
            }
        }
        //cnt = vec1.size() + vec2.size();
        // for(vector<int> vec : vec1){
        //     cnt += 1;
        //     for(int x : vec){
        //         answer[x] = cnt;
        //     }
        // }
        // for(vector<int> vec : vec2){
        //     cnt += 1;
        //     for(int x : vec){
        //         answer[x] = cnt;
        //     }
        // }
        cout << cnt << '\n';
        for(int x:answer){
            cout << x << ' ';
        }
        cout << '\n';
    }
    return 0;
}