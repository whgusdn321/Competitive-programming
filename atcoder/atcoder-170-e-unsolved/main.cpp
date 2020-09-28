#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, q;
    unordered_map<int, int> ctorm;
    unordered_map<int, int> ctosc;
    vector<multiset<int, greater<int>>> kinder(200001, multiset<int, greater<int>>());
    multiset<int, less<int>> supers;
    vector<int> answer;
    cin >> n >> q;
    for(int child=1; child<=n; child++){
        int score, garden;
        cin >> score >> garden;
        ctorm[child] = garden;
        ctosc[child] = score;
        kinder[garden].insert(score);
    }
     
    for(int i=1; i<200001; i++){
        if(!kinder[i].empty()){
            supers.insert(*kinder[i].begin());
        }
    }
    for(int i=0; i<q; i++){
        int c, d;
        cin >> c >> d;
        // cout << "i is : " << i << " c is : " << c << " d is : " << d << '\n';
        int room = ctorm[c];
        int nroom = d;
        int score = ctosc[c];
        int beforemax = *kinder[room].begin(); // 4208
        supers.erase(supers.find(beforemax));  //now super has {3056}
        kinder[room].erase(kinder[room].find(score));
        //now, kinder[room] can be empty
        if(!kinder[room].empty())
            supers.insert(*kinder[room].begin());
        if(!kinder[nroom].empty())
            supers.erase(supers.find(*kinder[nroom].begin()));
        kinder[nroom].insert(score);
        supers.insert(*kinder[nroom].begin()); // now super has {3056, 4208}
        answer.push_back(*supers.begin());
        ctorm[c] = nroom;
    }
    for(int ans : answer)
        cout << ans << '\n';
    return 0;
}

