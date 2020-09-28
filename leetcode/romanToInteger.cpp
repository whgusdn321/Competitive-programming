class Solution {
public:
    int romanToInt(string s) {
        int ret = 0;
        for(int i=0; i<s.size(); i++){
            if(s[i] == 'I'){
                if(i+1 < s.size() && s[i+1] == 'V'){
                    ret += 4;
                    i++;
                }
                else if(i+1 < s.size() && s[i+1] == 'X'){
                    ret += 9;
                    i++;
                }
                else{
                    ret += 1;
                }
            }
            else if(s[i] == 'V'){
                ret += 5;
            }
            else if(s[i] == 'X'){
                if(i+1 < s.size() && s[i+1] == 'L'){
                    ret += 40;
                    i++;
                }
                else if(i+1 < s.size() && s[i+1] == 'C'){
                    ret += 90;
                    i++;
                }
                else{
                    ret += 10;
                }
            }
            else if(s[i] == 'L'){
                ret += 50;
            }
            else if(s[i] == 'C'){
                if(i+1 < s.size() && s[i+1] == 'D'){
                    ret += 400;
                    i++;
                }
                else if(i+1 < s.size() && s[i+1] == 'M'){
                    ret += 900;
                    i++;
                }
                else{
                    ret += 100;
                }
            }
            else if(s[i] == 'D'){
                ret += 500;
            }
            else if(s[i] == 'M'){
                ret += 1000;
            }
            else{;}
        }
        return ret;
    }
};
