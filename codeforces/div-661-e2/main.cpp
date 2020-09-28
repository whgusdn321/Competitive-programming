#include <bits/stdc++.h>

using namespace std;

bool visited[100001];
map<pair<long long, long long>, long long> weights;
map<pair<long long, long long>, long long> costs;
priority_queue<vector<long long>> pq_ones, pq_twos;

long long sum = 0;

long long dfs(long long node, vector<vector<long long>> &tree){
    visited[node] = true;
    long long whole_nodes = 0;
    for(long long child : tree[node]){
        long long nodes = 0;
        if(!visited[child]){
            nodes = dfs(child, tree);
            long long weight = weights[{node, child}];
            long long cost = costs[{node, child}];
            if(cost == 1)
                pq_ones.push({nodes*weight - ((weight/2)*nodes), nodes, weight});
            else
                pq_twos.push({nodes*weight - ((weight/2)*nodes), nodes, weight});
            whole_nodes += nodes;
            sum += nodes*weight;
        }
    }
    if(whole_nodes == 0)
        return 1;
    else
        return whole_nodes;
}

void f(priority_queue<vector<long long>> &pq, long long &sum){
    
    vector<long long> tmp = pq.top();
    pq.pop();
    long long factor = tmp[0];
    long long weight = tmp[2];
    long long nodes = tmp[1];
    cout << "factor : " << factor << " weight : " << weight << " nodes : " << nodes << '\n';
    cout << "\n";
    long long new_weight = weight/2;
    long long diff = new_weight*nodes - ((new_weight/2)*nodes);
        
    vector<long long> tmp2{diff, nodes, new_weight};
    sum -= factor;
    pq.push(tmp2);
}

long long calc_diff(vector<long long> tmp){
    long long factor = tmp[0];
    long long weight = tmp[2];
    long long nodes = tmp[1];
    long long new_weight = weight/2;
    long long diff = new_weight*nodes - ((new_weight/2)*nodes);
    return diff;
}

//void print(){
//    
//}
void solve(){
    long long n = 0;
    long long s = 0;
    long long cnt = 0;
    long long cost = 0;
    sum = 0;
    fill(visited, visited+100001, false);
    weights.clear();
    costs.clear();
    pq_ones = priority_queue<vector<long long>>();
    pq_twos = priority_queue<vector<long long>>();
    cin >> n >> s;
    //make tree
    vector<vector<long long>> tree(n+1, vector<long long>());
    for(long long i=0; i<n-1; i++){ 
        long long a, b, weight, c;
        cin >> a >> b >> weight >> c;
        tree[a].push_back(b);
        tree[b].push_back(a);
        weights[{a, b}] = weight;
        weights[{b, a}] = weight;
        costs[{a, b}] = c;
        costs[{b, a}] = c; 
    }    
    // make priority queue
    
    dfs(1, tree);
    
    
    while(sum > s){
        cout << " sum is : " << sum << " s is : " << s << '\n';
        // vector<long long> tmp = pq.top();
        // pq.pop();
        // long long factor = tmp[0];
        // long long weight = tmp[2];
        // long long nodes = tmp[1];
        // long long new_weight = weight/2;
        // long long diff = new_weight*nodes - ((new_weight/2)*nodes);
        // 
        // vector<long long> tmp2{diff, nodes, new_weight};
        // sum -= factor;
        // pq.push(tmp2);
        // cnt += 1;
        if(pq_twos.size() == 0){ // select ones
            cout << "one is selected !" << '\n';
            f(pq_ones, sum);
            cost += 1;
        }
        else if(pq_ones.size() == 0){
            cout << "two is selected !" << '\n';
            f(pq_twos, sum);
            cost += 2;
        }
        else if(pq_ones.size() == 1){
            vector<long long> tmp_one = pq_ones.top();
            vector<long long> tmp_two = pq_twos.top();
            if(sum - pq_ones.top()[0] <= s){
                cout << "hihihihi ! one is selected !" << '\n';
                f(pq_ones, sum);
                cost += 1;
            }
            else if(tmp_one[0] >= tmp_two[0]){
                cout << "one is selected !" << '\n';
                f(pq_ones, sum);
                cost += 1;
            }
            else{
                cout << "two is selected !" << '\n';
                f(pq_twos, sum);
                cost += 2;
            }
        }
        else if(sum - pq_ones.top()[0] <= s){
            cout << "hihi ! one is selected !" << '\n';
            f(pq_ones, sum);
            cost += 1;
        }
        else if(pq_ones.top()[0] >= pq_twos.top()[0]){
            cout << "this is it !" << '\n';
            f(pq_ones, sum);
            cost += 1;
        }
        else{
            vector<long long> tmp_one1 = pq_ones.top();
            pq_ones.pop();
            vector<long long> tmp_one2 = pq_ones.top();
            pq_ones.push(tmp_one1);
            long long one_diff = max(tmp_one1[0] + calc_diff(tmp_one1),
                                     tmp_one1[0] + tmp_one2[0]);
            //pq_ones.push(tmp_one1);
            vector<long long> tmp_two = pq_twos.top();
            if(tmp_two[0] >= one_diff){
                cout << "two is selected !" << '\n';
                f(pq_twos, sum);
            }
            else{
                cout << "!!!two ones is selected !" << '\n';
                cout << "one_diff is : " << one_diff << '\n';
                f(pq_ones, sum);
                f(pq_ones, sum);
            }
            cost += 2;
        }
    }
    cout << cost << '\n';
    
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
