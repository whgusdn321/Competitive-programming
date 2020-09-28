class Solution {
public:
    string longestPalindrome(string s) {
        string ans = s.substr(0, 1);
        for(int i=0; i<s.size(); i++){
            int length = 1;
            int mid = i;
            int left = mid - 1, right = mid + 1;
            while(left >= 0 && right < s.size() && s[left] == s[right]){
                length += 2;
                left--;
                right++;
            }
            if(length > ans.size())
                ans = s.substr(left+1, length);
            
            // ?? 
            if(mid + 1 < s.size() && s[mid] == s[mid+1]){
                length = 2;
                left = mid - 1;
                right = mid + 2;
                while(left >= 0 && right < s.size() && s[left] == s[right]){
                    left--;
                    right++;
                    length+=2;
                }
                if(length > ans.size())
                    ans = s.substr(left+1, length);
            }
        }
        return ans;
    }
};
