#include <string>
#include <vector>
#include <algorithm>

using namespace std;
bool cmp(const vector<int>& a, const vector<int>& b){
    return a[2] < b[2];
}
int solution(int n, vector<vector<int>> costs) {
    int ans = 0;
    sort(costs.begin(), costs.end(), cmp);
    bool visited[n];
    fill(visited, visited+n, false);
    // for(int i=0; i<costs.size(); i++)
    //     printf("(%d, %d, %d)\n",costs[i][0], costs[i][1], costs[i][2]);
    int j = 0;
    int i = 0;
    while (i < n){
        vector<int> arry = costs[j];
        int node1 = arry[0];
        int node2 = arry[1];
        int cost = arry[2];
        if (!visited[node1] or !visited[node2]){
            if (!visited[node1]){
                visited[node1] = true;
                i += 1;
            }
            if (!visited[node2]){
            	visited[node2] = true;
                i += 1;
            }
            ans += cost;
        }
        j += 1;
    }
    return ans;
}