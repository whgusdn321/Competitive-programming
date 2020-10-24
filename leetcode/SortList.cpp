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
    ListNode* sortList(ListNode* head) {
        if(head == NULL || head->next == NULL)
            return head;
        ListNode *mid = getMid(head);
        ListNode *l = sortList(head);
        ListNode *r = sortList(mid);
        ListNode *ret = merge(l, r);
        return ret;
    }
    ListNode* getMid(ListNode *head){
        ListNode *mid = NULL;
        while(head && head->next){
            if(mid == NULL)
                mid = head;
            else
                mid = mid->next;
            head = head->next->next;
        }
        ListNode *rmid = mid->next;
        mid->next = NULL;
        return rmid;
    }
    
    ListNode* merge(ListNode *left, ListNode *right){
        ListNode ret(0);
        ListNode *last = &ret;
        
        while(left && right){
            if(left->val < right->val){
                last->next = left;
                last = last->next;
                left = left->next;
            }
            else{
                last->next = right;
                last = last->next;
                right = right->next;
            }
        }
        if(left)
            last->next = left;
        else
            last->next = right;
        return ret.next;
    }
};
