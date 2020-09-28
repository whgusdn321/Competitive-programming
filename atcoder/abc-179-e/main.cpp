#include <bits/stdc++.h>

using namespace std;

int main()
{
    long long n;
    int x, m;
    int val2idx[100001];
    long long idx2val[100001];
    fill(val2idx, val2idx+100001, 0);
    fill(idx2val, idx2val+100001, 0);
    
    cin >> n >> x >> m;
    val2idx[x] = 1;
    idx2val[1] = x;
    long long next = x;
    long long ans = x;
    for(long long i=2; i<=n; i++){
        //cout << "i : " << i << '\n';
        next = (next * next) % m;
        //ans += next;
        
        if(val2idx[next]){
            long long sum = 0;
            for(long long j=val2idx[next]; j<i; j++){
                sum += idx2val[j];
            }
            long long length = i - val2idx[next];
            long long togo = n - i + 1;
            //cout << "before ans : " << ans << '\n';
            ans += (togo/length)*sum;
            //cout << "after ans : " << ans << '\n';
            for(long long j=val2idx[next]; j<val2idx[next]+togo%length; j++){
                ans += idx2val[j];
            }
            //cout << "aftter ans : " << ans << '\n';
            break;
        }
        else{
            ans += next;
            val2idx[next] = i;
            idx2val[i] = next;
        }
    }
    cout << ans << '\n';
    return 0;
}
