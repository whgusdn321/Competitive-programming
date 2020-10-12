class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        bool pos = false;
        int n = bits.size();
        for(int i=0; i<n; i++){
            if(bits[i] == 1){
                i += 1;
            }
            else{
                if(i==n-1)
                    pos = true;
            }
        } 
        return pos;
    }
};
