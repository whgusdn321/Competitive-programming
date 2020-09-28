#include <bits/stdc++.h>

using namespace std;

int h, w, sy, sx, gy, gx;
char m[1000][1000];
bool visited[1000][1000];
int dy[4] = {1, 0, -1, 0};
int dx[4] = {0, -1, 0, 1};
int ans = -1;
vector<pair<int, int>> vst, next_vst;

void go(int y, int x, int cnt){
    visited[y][x] = true;
    next_vst.push_back({y, x});
    if(y == gy && x == gx){
        ans = cnt;
        return;
    }
    for(int i=0; i<4; i++){
        int ny = y + dy[i];
        int nx = x + dx[i];
        if(0 <= ny && ny < h && 0 <= nx && nx < w && !visited[ny][nx]
        && m[ny][nx] == '.'){
            go(ny, nx, cnt);
        }
    }    
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> h >> w;
    cin >> sy >> sx;
    cin >> gy >> gx;
    sy--; sx--; gy--; gx--;
    for(int i=0; i<h; i++){
        for(int j=0; j<w; j++){
            cin >> m[i][j];
            //cout << m[i][j] << ' ';
        }
        //cout << '\n';
    }
    int cnt = 0;
    vst.push_back({sy, sx});
    while(!vst.empty()){
        for(int i=0; i<vst.size(); i++){
            pair<int, int> p = vst[i];
            sy = p.first;
            sx = p.second;
            if(!visited[sy][sx])
                go(sy, sx, cnt);
        }
        vst.clear();
        for(int i=0; i<next_vst.size(); i++){
            pair<int, int> p = next_vst[i];
            int y = p.first;
            int x = p.second;
            for(int ny = y-2; ny <= y+2; ny++){
                for(int nx = x-2; nx <= x+2; nx++){
                    if(0 <= ny && ny < h && 0 <= nx && nx < w && !visited[ny][nx]
                    && m[ny][nx] == '.'){
                        vst.push_back({ny, nx});
                    }
                }
            }       
        }
        next_vst.clear();
        cnt++;
    }
    cout << ans << '\n';
    return 0;
}
