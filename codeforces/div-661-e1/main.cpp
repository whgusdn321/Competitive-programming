#include <bits/stdc++.h>

using namespace std;

bool visited[100001];
map<pair<long long, long long>, long long> weights;
priority_queue<vector<long long>> pq;

long long sum = 0;

long long dfs(long long node, vector<vector<long long>> &tree){
    visited[node] = true;
    long long whole_nodes = 0;
    for(long long child : tree[node]){
        long long nodes = 0;
        if(!visited[child]){
            nodes = dfs(child, tree);
            long long weight = weights[{node, child}];
            pq.push({nodes*weight - ((weight/2)*nodes), nodes, weight});
            whole_nodes += nodes;
            sum += nodes*weight;
        }
    }
    if(whole_nodes == 0)
        return 1;
    else
        return whole_nodes;
}
void solve(){
    long long n = 0;
    long long s = 0;
    long long cnt = 0;
    sum = 0;
    fill(visited, visited+100001, false);
    weights.clear();
    pq = priority_queue<vector<long long>>();
    cin >> n >> s;
    //make tree
    vector<vector<long long>> tree(n+1, vector<long long>());
    for(long long i=0; i<n-1; i++){ 
        long long a, b, weight;
        cin >> a >> b >> weight;
        tree[a].push_back(b);
        tree[b].push_back(a);
        weights[{a, b}] = weight;
        weights[{b, a}] = weight;
    }    
    // make priority queue
    
    dfs(1, tree);
    
    
    while(sum > s){
        vector<long long> tmp = pq.top();
        pq.pop();
        long long factor = tmp[0];
        long long weight = tmp[2];
        long long nodes = tmp[1];
        long long new_weight = weight/2;
        long long diff = new_weight*nodes - ((new_weight/2)*nodes);
        
        vector<long long> tmp2{diff, nodes, new_weight};
        sum -= factor;
        pq.push(tmp2);
        cnt += 1;
    }
    cout << cnt << '\n';
    
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long tc;
    cin >> tc;
    for(long long t=0; t<tc; t++){
        solve();
    }
    return 0;
}
