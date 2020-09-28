/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        //ListNode* ret = NULL;
        ListNode *r1 = l1, *r2 = l2;
        ListNode *ret = new ListNode((r1->val + r2->val)%10);
        ListNode *last = ret;
        int plus = (r1->val + r2->val)/10;
        r1 = r1->next;
        r2 = r2->next;
        while(r1 != NULL || r2 != NULL || plus){
            int a=0, b=0, tmp=0;
            if(r1 != NULL)
                a = r1->val;
            if(r2 != NULL)
                b = r2->val;
            //cout << "a : " << a << " b : " << b << " plus : " << plus << '\n';
            tmp = a + b + plus;
            plus = tmp / 10;
            tmp = tmp %= 10;
            ListNode *newNode = new ListNode(tmp);
            last->next = newNode;
            last = last->next;
            if(r1!=NULL)
                r1 = r1->next;
            if(r2!=NULL)
                r2 = r2->next; 
        }
        return ret;
    }
};
