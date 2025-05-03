#include "main.hpp"

ListNode* removeElements(ListNode *head, int val) {
    if(head == nullptr) {
        return head;
    }
    if(head->next == nullptr && head->val == val) {
        return nullptr;
    }

    ListNode temp(0);
    ListNode *tempPtr = &temp;
    ListNode *curr = head;
    while(curr != nullptr) {
        if(curr->val != val) {
            tempPtr->next = curr;
            tempPtr = tempPtr->next;
        }
        curr = curr->next;
    }

    tempPtr->next = nullptr;
    return temp.next;
}