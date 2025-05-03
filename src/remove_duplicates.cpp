#include "main.hpp"

ListNode* deleteDuplicates(ListNode *head) {
    if(head == nullptr || head->next == nullptr) {
        return head;
    }

    ListNode *curr = head;
    while(curr->next != nullptr) {
        if(curr->val == curr->next->val) {
            curr->next = curr->next->next;
        } else {
            curr = curr->next;
        }
    } 

    return head;
}