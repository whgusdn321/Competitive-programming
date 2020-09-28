#include <bits/stdc++.h>

using namespace std;

int find(int n){
    int div1, div2;
    vector<int> vec;
    for(int i=2; i*i<=n; i++){
        if(n%i == 0){
            div1 = i;
            div2 = n/i;
            if(div1 % 2){
                vec.push_back(div1);
            }
            else if(div2 %2){
                vec.push_back(div2);
            }
            else{
            ;}
        }
    }
    if(!vec.empty())
        return *min_element(vec.begin(), vec.end());
    else
        return 0;
}

int main()
{
    int tc;
    cin >> tc;
    for(int i=0; i<tc; i++){
        int n;
        int cnt = 0;
        cin >> n;
        if(n == 1){
            cout << "FastestFinger" << '\n';
            continue;
        }
        while(1){
            if(n == 2 || n%2){
                cnt++;
                break;
            }
            else{ // 짝수
                int k = 0;
                k = find(n);
                if(k){
                    n/=k;
                    cnt++;
                }
                else{
                    n--;
                    cnt++;
                }
            }
        }
        if(cnt%2){
            cout << "Ashishgup" << '\n';
        }
        else{
            cout << "FastestFinger"<< '\n';
        }
        
        
    }
    return 0;
}
