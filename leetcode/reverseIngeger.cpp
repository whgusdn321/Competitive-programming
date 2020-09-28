class Solution {
public:
    int reverse(int x) {
        //cout << "x : " << x << '\n';
        long long c = -((long long)1<<31);
        if(x == c)
            return 0;
        
        long long mul = 1; 
        bool negative = false;
        if(x < 0){
            negative = true;
            x *= -1;
        }
        
        //int n = 0;
        long long div = 1;
        int xx = x;
        while(xx > 0){
            //n++;
            div *= 10;
            xx /= 10;
        }
        // cout << div << '\n';
        div /= 10;
        long long ans = 0;
        
        while(x){
            int digit = x / div;
            x %= div;
            ans += mul*digit;
            mul *= 10;
            div /= 10;
        }
        if(negative)
            ans *= -1;
        if(-((long long)1<<31) <= ans && ans <= ((long long)1 << 31) -1)
            return ans;
        else
            return 0;
    }
};
