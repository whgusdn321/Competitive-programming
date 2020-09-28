class Solution {
public:
    int mySqrt(int x) {
        if(x == 1)
            return 1;
        long long l = 1;
        long long r = x;
        
        long long ans;
        while(true){
            long long m = (l+r)/2;
            if( m*m <= x && x < (m+1)*(m+1)){
                ans = m;
                break;
            }
            else if( x < m*m){
                r = m-1;
            }
            else{
                l = m+1;
            }
                
        }
        return ans;
    }
};
