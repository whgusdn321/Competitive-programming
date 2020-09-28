#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, k;
    int p[5001];
    int c[5001];
    long long ans[5001];
    
    cin >> n >> k;
    for(int i=0; i<n; i++)
        cin >> p[i];
    for(int i=0; i<n; i++)
        cin >> c[i];    
    
    map<pair<int, int>, long long> dict1; // for <index, length, scores>
    // unordered_map<int, int> dict2; // for index, length
    for(int i=0; i<n; i++){
        int cur = i; 
        int length = 0;
        long long scores_sum = 0;
        long long max_scores = -1e9-10;
        int visited[5001] = {false};
        long long scores[5001] = {0};
        do{ 
            visited[cur] = length;
            scores[cur] = scores_sum;
            
            // progress 
            length++;
            cur = p[cur] - 1;
            scores_sum += c[cur];
            max_scores = max(max_scores, scores_sum);
            // cout << "cur is : " << cur << " scores is : " << scores << '\n';
        }while(!visited[cur] && length < k);
        
        if(length == k){
            ans[i] = max_scores;
        }
        else{ // looping
            long long loop_scores = scores_sum - scores[cur];
            long long loop_length = length - visited[cur];
            if(loop_scores <= 0){
                ans[i] = max_scores;
            }
            else{
                long long left = k - length;
                int times = left / loop_length;
                int d = left % loop_length;
                ans[i] = scores + loop_scores*;
            }
        }
    }
    // for(int i=0; i<n; i++)
    //     cout << ans[i] << ' ';
    // cout << '\n';
    cout << *max_element(ans, ans+n) << '\n';
    return 0;
}
