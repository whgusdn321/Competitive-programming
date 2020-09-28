#include <bits/stdc++.h>

using namespace std;

int main(){
    map<int, int> dict;
    int n;
    cin>>n;
    for(int i=0; i<n; i++){
        int l;
        cin >> l;
        dict[l] += 1;
    }
    int eights = 0, fours = 0, six = 0, twos = 0;
    for(auto it=dict.begin(); it!=dict.end(); it++){
        if(it->second >=8){
            eights += 1;
        }
        else if(it->second >= 6){
            six += 1;
        }
        else if(it->second >= 4){
            fours += 1;
        }
        else if(it->second >= 2){
            twos += 1;
        }
        else {;}
    }
    int q;
    cin >> q;
    for(int i=0; i<q; i++){
        char oper;
        int n;
        cin >> oper >> n;
        if(oper == '-'){
            if(dict[n] == 8){
                eights -=1;
                six += 1;
            }
            if(dict[n] == 6){
                six -= 1;
                fours += 1;
            }
            else if(dict[n] == 4){
                fours -= 1;
                twos += 1;
            }
            else if(dict[n] == 2){
                twos -= 1;
            }
            else{;}
            dict[n] -= 1;
        }
        else{ // '+'
            if(dict[n] == 1){
                twos += 1;
            }
            else if(dict[n] == 3){
                twos -= 1;
                fours += 1;
            }
            else if(dict[n] == 5){
                fours -= 1;
                six += 1;
            }
            else if(dict[n] == 7){
                six -= 1;
                eights += 1;
            }
            else{;}
            dict[n] += 1;
        }
        if((eights >= 1) || (fours >= 1 && twos >=2) || (six >= 1 && twos >= 1) || (fours >= 2) || (fours >=1 && six >=1) || (six >= 2)){
            cout << "YES" << '\n';
        }
        else{
            cout << "NO" << '\n';
        }
    }
    
    return 0;
}

