class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows==1)
            return s;
        string ss[numRows];
        int y = 0;
        int dy = 1;
        for(int i=0; i<s.size(); i++){
            ss[y] += s[i];
            if(y == numRows-1 || (y == 0 && i != 0))
                dy *= -1;
            y += dy;
        }
        string ans;
        for(int i=0; i<numRows; i++)
            ans += ss[i];
        return ans;
        
    }
};
