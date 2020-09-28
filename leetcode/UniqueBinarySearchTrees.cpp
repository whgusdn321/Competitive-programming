class Solution {
public:
    long long memo[20];
    int numTrees(int n) {
        if(n == 1 || n == 0){
            memo[n] = 1;
            return memo[n];
        }
        else{
            if(memo[n] != 0)
                return memo[n];
            int s = n-1;        
            int cnt = n;
            long long tmp = 0;
            while(cnt > 1){
                tmp += 2*numTrees(s)*numTrees(n-1-s);
                cnt -= 2;
                s--;
            }
            if(cnt == 1)
                tmp += numTrees(s) * numTrees(n-1-s);
            memo[n] = tmp;
            return memo[n];
        }
    }
};
