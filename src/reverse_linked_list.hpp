#include "main.hpp"

ListNode* reverseList(ListNode *head) {
    if(head == nullptr || head->next == nullptr) {
        return head;
    }

    ListNode *prev = nullptr;
    ListNode *curr = head;
    while(curr != nullptr) {
        ListNode *next = curr->next;
        curr->next = prev;

        prev = curr;
        curr = next;
    }

    return prev;
}