#include <bits/stdc++.h>

using namespace std;

int N[100001];
bool visited[100001];

bool bfs(vector<vector<int>> &graph, int n){
    queue<vector<int>> qu;
    qu.push({1, 1});
    visited[1] = true;
    int cnt = 0;
    while(!qu.empty()){
        vector<int> node = qu.front();
        qu.pop();
        cnt++;
        N[node[0]] = node[1];
        for(int child : graph[node[0]]){
            if(!visited[child]){
                visited[child] = true;
                qu.push({child, node[0]});
            }
        }
    }
    return cnt == n;    
}
int main()
{
    int n, m;
    cin >> n >> m;
    vector<vector<int>> graph(n+1);
    for(int i=0; i<m; i++){
        int a, b;
        cin >>a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    bool found = bfs(graph, n);
    if(found){
        cout << "Yes" << '\n';
        for(int i=2; i<=n; i++)
            cout << N[i] << '\n';
    }
    else
        cout << "No";
    return 0;
}
