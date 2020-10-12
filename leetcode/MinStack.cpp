typedef struct node {
    node* next = NULL;
    int val = 0;
}node;

class MinStack {
public:
    /** initialize your data structure here. */
    node *topp;
    MinStack() {
        topp = NULL;
    }
    
    void push(int x) {
        node *newnode = new node;
        newnode->next = topp;
        newnode->val = x;
        topp = newnode;
    }
    
    void pop() {
        if(topp == NULL)
            return;
        node *todel = topp;
        topp = todel->next;
        delete todel;
    }
    
    int top() {
        return topp->val;
    }
    
    int getMin() {
        int miin = INT_MAX;
        node *t = topp;
        while(t != NULL){
            int val = t->val;
            miin = min(miin, val);
            t = t->next;
        }
        return miin;
    }
};

