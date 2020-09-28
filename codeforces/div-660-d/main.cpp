#include <bits/stdc++.h>

using namespace std;

deque<long long> fridge1(0), fridge2(0);
long long n;
long long a[200001];
long long b[200001];
bool visited[200001];
vector<long long> minus_ones;
//vector<vector<long long>> tree(200001, vector<long long>(0));

void print(deque<long long> & a){
    cout << "print : " << '\n';
    for(int x : a)
        cout << x << ' ';
    cout << "\n";
}

long long dfs(long long node, vector<vector<long long>> &tree){
    visited[node] = true;
    long long sum = 0;
    for(long long child : tree[node]){
        if(!visited[child])
            sum += dfs(child, tree);
    }
    sum += a[node];
    fridge1.push_back(node);
    if(sum >= 0){
        return sum;
    }
    else{ // sum < 0 
        //print(fridge1);
        while(!fridge1.empty()){
            long long tmp = fridge1.back();
            fridge1.pop_back();
            fridge2.push_front(tmp);
        }
        return 0;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    fill(visited, visited+200001, false);
    cin >> n;
    vector<vector<long long>> tree(n+1, vector<long long>(0));
    for(long long i=0; i<n; i++){
        cin >> a[i+1];
    }
    //make tree
    for(long long i=0; i<n; i++){
        cin >> b[i+1];
        if(b[i+1] == -1){
            minus_ones.push_back(i+1);
        }
        else{
            tree[i+1].push_back(b[i+1]);
            tree[b[i+1]].push_back(i+1);
        }
    }
    
    for(long long minus : minus_ones){
        // cout << "minus is : " << minus << '\n';
        if(!visited[minus]){
            dfs(minus, tree);
            while(!fridge1.empty()){
                long long tmp = fridge1.back();
                fridge1.pop_back();
                fridge2.push_front(tmp);
            }
        }
    }    
    
    // cout << "fridge2 is : " << '\n';
    long long ans = 0;
    for(long long idx : fridge2){
        ans += a[idx];
        if(b[idx] != -1)
            a[b[idx]] += a[idx];
    }
    cout << ans << '\n';
    for(long long idx : fridge2){
        cout << idx << ' ';
    }
    return 0;
}
