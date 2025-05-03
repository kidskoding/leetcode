#include "main.hpp"

ListNode* swapPairs(ListNode *head) {
    if(head == nullptr || head->next == nullptr) {
        return head;
    }

    ListNode temp(0);
    temp.next = head;

    ListNode *prevNode = &temp;
    ListNode *currNode = head;
    while(currNode != nullptr && currNode->next != nullptr) {
        ListNode *first = currNode;
        ListNode *second = currNode->next;

        ListNode *nextPair = second->next;

        prevNode->next = second;
        second->next = first;
        first->next = nextPair;

        prevNode = first;
        currNode = nextPair;
    }

    return temp.next;
}