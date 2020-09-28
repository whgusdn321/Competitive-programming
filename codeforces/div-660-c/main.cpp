#include <bits/stdc++.h>

using namespace std;

bool found = false;
long long cities[100001];
long long happiness[100001];
bool visited[100001];

vector<long long> go(int node, vector<vector<int>> &tree){
    long long left=0, right=0;
    visited[node] = true;
    for(int child : tree[node]){
        if(!visited[child]){
            vector<long long> tmp = go(child, tree);
            left += tmp[0];
            right += tmp[1];
        }
    }
    if(found) 
        return {0, 0};
        
    left += cities[node];
    long long right_bound = right + left; //+cities[node];
    long long left_bound = right - left;
    if(left_bound <= happiness[node] && happiness[node] <= right_bound &&
        (happiness[node] - left_bound)%2==0)
    {
        long long x = (happiness[node] - left_bound)/2;
        left -= x;
        right += x;
        return {left, right};
    }
    else{
        found = true;
        return {0, 0};
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int tc;
    cin >> tc;
    // int cites[10001];
    // int happiness[10001];
    int n, m;
    for(int t=0; t<tc; t++){
        cin >> n >> m;                                                  
        fill(visited, visited+n+1, false);
        vector<vector<int>> tree(n+1, vector<int>(0));
        for(int i=0; i<n; i++){
            cin >> cities[i+1];
        }
        for(int i=0; i<n; i++){
            cin >> happiness[i+1];
        }
        for(int i=0; i<n-1; i++){
            int node1, node2;
            cin >> node1 >> node2;
            tree[node1].push_back(node2);
            tree[node2].push_back(node1);
        }
        found = false;
        vector<long long> vec = go(1, tree);
        if(found)
            cout << "NO" << '\n';
        else
            cout << "YES" << '\n';
    }
    return 0;
}