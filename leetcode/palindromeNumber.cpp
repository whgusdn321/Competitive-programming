class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0)
            return false;

        long long mul = 1;
        long long xx = x;
        long long y = 0;        
        
        while(xx > 9){
            mul *= 10;
            xx /= 10;
        }
        xx = x;
        while(xx){
            y += mul*(xx%(10));
            xx /= 10;
            mul /= 10;
        }
        //cout << x  << ' '<<  y << '\n';
        return x == y;
            
    }
};
