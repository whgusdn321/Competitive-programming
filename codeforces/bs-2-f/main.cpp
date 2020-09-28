#include <bits/stdc++.h>

using namespace std;

string t, p;
vector<int> todel;

bool f(int mid){
    // make new word;
    string new_word;
    vector<bool> visited(t.size(), false);
    for(int i=0; i<mid; i++){
        visited[todel[i]-1] = true;
    }
    for(int i=0; i<t.size(); i++){
        if(!visited[i])
            new_word += t[i];
    }
    int i = 0;
    int k = 0;
    for(int i=0; i<new_word.size(); i++){
        if(new_word[i] == p[k]){
            k++;
            if(k == p.size()){
                break;
            }
        }
    }
    return p.size() == k;
}

int main()
{
    cin >> t;
    cin >> p;
    for(int i=0; i<t.size(); i++){
        int n;
        cin >> n;
        todel.push_back(n);
    }
    int l = 0;
    int r = t.size();
    while(l < r-1){
        int mid = (l+r)/2;
        if(f(mid)){
            l = mid;
        }
        else{
            r = mid;
        }
    }
    cout << l << '\n';
    return 0;
}
