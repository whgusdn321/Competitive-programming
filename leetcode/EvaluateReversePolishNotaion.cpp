class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        if(tokens.empty())
            return 0;
        stack<int> stakk;
        for(string x: tokens){
            if(x == "+"){
                int b = stakk.top();                 
                stakk.pop();
                int a = stakk.top();
                stakk.pop();
                stakk.push(a+b);
            }
            else if(x == "-"){
                int b = stakk.top();                 
                stakk.pop();
                int a = stakk.top();
                stakk.pop();
                stakk.push(a-b);
            }
            else if(x == "*"){
                int b = stakk.top();                 
                stakk.pop();
                int a = stakk.top();
                stakk.pop();
                stakk.push(a*b);
            }
            else if(x == "/"){
                int b = stakk.top();                 
                stakk.pop();
                int a = stakk.top();
                stakk.pop();
                stakk.push(a/b);
            }
            else{
                stakk.push(stoi(x));
            }
        }
        return stakk.top();
    }
};
