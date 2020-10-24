class Solution {
public:
    bool pos(vector<int> &vec){
        int a = vec[0];
        for(int i=1; i<vec.size(); i++){
            if(vec[i] != a)
                return false;
        }
        return true;
    }
    
    int minDominoRotations(vector<int>& A, vector<int>& B) {
        vector<vector<int>> as(7, vector<int>());
        vector<vector<int>> bs(7, vector<int>());
        
        int n = A.size();
        int ans = 1e5;
        for(int i=0; i<n; i++){
            as[A[i]].push_back(i);
        }
        for(int i=0; i<n; i++){
            bs[B[i]].push_back(i);
        }
        
        for(int i=1; i<=6; i++){
            int cnt = 0;
            for(int j=1; j<=6; j++){
                if(j != i){
                    for(int idx : as[j]){
                        int tmp = A[idx];
                        A[idx] = B[idx];
                        B[idx] = tmp;
                        cnt++;
                    }
                }
            }
            if(pos(A))
                ans = min(ans, cnt);
            for(int j=1; j<=6; j++){
                if(j != i){
                    for(int idx : as[j]){
                        int tmp = A[idx];
                        A[idx] = B[idx];
                        B[idx] = tmp;
                    }
                }
            }
            
            cnt = 0;
            for(int j=1; j<=6; j++){
                if(j != i){
                    for(int idx : bs[j]){
                        int tmp = A[idx];
                        A[idx] = B[idx];
                        B[idx] = tmp;
                        cnt++;
                    }
                }
            }
            if(pos(B))
                ans = min(ans, cnt);
            for(int j=1; j<=6; j++){
                if(j != i){
                    for(int idx : bs[j]){
                        int tmp = A[idx];
                        A[idx] = B[idx];
                        B[idx] = tmp;
                    }
                }
            }
        }
        if(ans == 1e5)
            return -1;
        else
            return ans;
    }
    
};
