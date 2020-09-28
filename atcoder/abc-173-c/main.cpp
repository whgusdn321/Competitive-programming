#include <bits/stdc++.h>

using namespace std;

int h, w, k;

void combi(int before, int n, int r, vector<vector<int> > & vec, vector<int> & tmp){
    if(tmp.size() == r){
        vector<int> to_copied = tmp;
        vec.push_back(to_copied);
        return;
    }
    for(int i=before+1; i<n; i++){
        tmp.push_back(i);
        combi(i, n, r, vec, tmp);
        tmp.pop_back();
    }
}

void color1(vector<vector<char>> &maap, vector<int> row){
    for(int i:row){
        for(int j=0; j<w; j++){
            maap[i][j] = 'r';
        }
    }    
}

void color2(vector<vector<char>> &maap, vector<int> col){
    for(int i=0; i<h; i++){
        for(int j : col){
            maap[i][j] = 'r';
        }
    }    
}

int inspect(vector<vector<char>> &maap){
    int n = 0;
    for(int i=0; i<h; i++){
        for(int j=0; j<w; j++){
            if(maap[i][j] == '#')
                n++;
        }
    }
    return n;
}

int main()
{
    vector<vector<int>> rows, cols;
    vector<vector<char>> maap(6, vector<char>(6, '#'));
    cin >> h >> w >> k;
    for(int i=0; i<h; i++){
        for(int j=0; j<w; j++){
            cin >> maap[i][j];
        }
    }
    vector<int> tmp1, tmp2;
    int ans = 0;
    for(int r=0; r<=h; r++)
        combi(-1, h, r, rows, tmp1);
    for(int r=0; r<=w; r++)
        combi(-1, w, r, cols, tmp2);
    for(vector<int> row : rows){
        for(vector<int> col : cols){
            vector<vector<char> > tmp_map = maap;
            color1(tmp_map, row);
            color2(tmp_map, col);
            int n = inspect(tmp_map);
            if(n == k){
                // cout << "rows : " ;
                // for(int r : row) cout << r << ' ';
                // cout << "'\n cols : ";
                // for(int c : col) cout <<c << ' ';
                // cout << '\n';
                ans++;
            }
        }
    }
    cout << ans << '\n';
    return 0;
}