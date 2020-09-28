class Solution {
public:
    string intToRoman(int num) {
        map<int, string, greater<int> > dict = 
        {{1, "I"},
         {5, "V"},
         {10, "X"},
         {50, "L"},
         {100, "C"},
         {500, "D"},
         {1000, "M"},
         {4, "IV"},
         {9, "IX"},
         {40, "XL"},
         {90, "XC"},
         {400, "CD"},
         {900, "CM"}
        };
        string ret;
        
        for(auto it=dict.begin(); it!=dict.end(); it++){
            int n = it->first;
            string s = it->second;
            if(num/n > 0){
                for(int i=1; i<=num/n; i++)
                    ret += s;
            }
            num %= n;
        }
        return ret; 
    }
};
