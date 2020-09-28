#include <bits/stdc++.h>

using namespace std;

int H, W, k;
int _y1, x1, y2, x2;

int bfs(vector<vector<char>> & maap, vector<vector<bool>> & visited){
    queue<vector<int>> qu;
    qu.push({_y1, x1, 0});
    visited[_y1][x1] = true;
    while(!qu.empty()){
        int ty = qu.front()[0];
        int tx = qu.front()[1];
        int cnt = qu.front()[2];
        qu.pop();

        if(ty == y2 && tx == x2){
            return cnt;
        }
        for(int ny = ty; ny <=ty+k; ny++){
            if(ny < H && maap[ny][tx] == '@')
                break;
            if(ny < H && !visited[ny][tx] && maap[ny][tx] != '@'){
                visited[ny][tx] = true;
                qu.push({ny, tx, cnt+1});
            }
        }
        for(int ny = ty; ny >= ty-k; ny--){
            if(ny >= 0 && maap[ny][tx] == '@')
                break;
            if(ny >=0 && !visited[ny][tx] && maap[ny][tx] != '@'){
                visited[ny][tx] = true;
                qu.push({ny, tx, cnt+1});
            }
        }
        for(int nx = tx; nx <=tx+k; nx++){
            if(nx < W && maap[ty][nx] == '@')
                break;
            if(nx < W && !visited[ty][nx] && maap[ty][nx] != '@'){
                visited[ty][nx] = true;
                qu.push({ty, nx, cnt+1});
            }
        }
        for(int nx = tx; nx >= tx-k; nx--){
            if(nx >= 0 && maap[ty][nx] == '@')
                break;
            if(nx >= 0 && !visited[ty][nx] && maap[ty][nx] != '@'){
                visited[ty][nx] = true;
                qu.push({ty, nx, cnt+1});
            }
        }
            
    }
    return -1;
    
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> H >> W >> k;
	cin >> _y1 >> x1 >> y2 >> x2;
	_y1--; x1--; y2--; x2--;
	vector<vector<char>> maap(H, vector<char>(W, 0));
	vector<vector<bool>> visited(H, vector<bool>(W, false));
	for (int i = 0; i < H; i++) {
		for (int j = 0; j <W; j++){
		    cin >> maap[i][j];    
		}
	}
    int ans = bfs(maap, visited);
    cout << ans;
	return 0;
}