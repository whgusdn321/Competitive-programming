#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    string s;
    for(int i=0; i<t; i++){
        int n;
        cin >> n;
        cin >> s;
        string stmp;
        vector<string> vec;
        
        for(int j=0; j < n; j++){
            stmp += s[j];
            if(j+1 == n || s[j+1] != stmp.back()){
                vec.push_back(stmp);
                stmp = "";
            }
        }
       
        if(vec.size() == 1){
            cout << vec[0] << '\n';
        }
        else if(vec.size() == 2){
            if(vec[0][0] == '0')
                cout<<vec[0] + vec[1] << '\n';
            else
                cout << '0' << '\n';
        }
        else{
            if(vec[0][0] == '0'){
                if((vec.size()-1) %2 == 0){
                    cout << vec[0] + '0' << '\n';
                }
                else{
                    cout << vec[0] +'0' + vec.back() << '\n';
                }
            }
            else{
                if((vec.size()) %2 == 0){
                    cout << '0' << '\n';
                }
                else{
                    cout << "0" + vec.back() << '\n';
                }
            }
        }
    }
    return 0;
}
