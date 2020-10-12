class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        int n = A.size();
        int ans = 0;
        unordered_map<int, int> dict;
        
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                int a = A[i] + B[j];
                dict[a] += 1;
            }
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                int b = C[i] + D[j];
                ans += dict[-b];
            }
        }
        return ans;
    }
};
