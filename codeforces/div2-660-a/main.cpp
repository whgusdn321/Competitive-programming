#include <bits/stdc++.h>

using namespace std;

void np(vector<int> & nearly_primes){
    int limit = 2e5;
    bool visited[200000];
    for(int i=2; i<=20000; i++){
        if(!visited[i]){
            nearly_primes.push_back(i);
            for(int j=i; j<=20000; j+=i){
                visited[j] = true;
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int tc;
    int n;
    cin >> tc;
    vector<int> primes, nearly_primes;
    np(primes);
    
    
    for(int i=0; i<primes.size()-1; i++){
        for(int j=i+1; j<primes.size(); j++){
            int tmp = primes[i] * primes[j];
            nearly_primes.push_back(tmp);
        }
    }
    sort(nearly_primes.begin(), nearly_primes.end());
    for(int t=0; t<tc; t++){
        cin >> n;
        bool found = false;
        for(int i=0; i<nearly_primes.size(); i++){
            if(found) break;
            for(int j=i+1; j<nearly_primes.size(); j++){
                if(found) break;
                for(int k=j+1; k<nearly_primes.size(); k++){
                    if(found) break;
                    
                    int a = nearly_primes[i];
                    int b = nearly_primes[j];
                    int c = nearly_primes[k];
                    int d = n - (a+b+c);
                    if(d <= 0){
                        cout << "NO" << '\n';
                        found = true;
                        break;
                    }
                    if(d != a && d!= b && d!=c){
                        cout <<"YES" << '\n' << a << ' ' << b << ' ' << c  << ' ' << d << '\n';
                        found = true;
                        break;
                        
                    }
                    
                }
            }
        }
         
    }
    return 0;
}
