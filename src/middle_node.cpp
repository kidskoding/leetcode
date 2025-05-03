#include "main.hpp"

ListNode* middleNode(ListNode *head) {
    ListNode *temp = head;
    int count = 0;
    while(temp != nullptr) { count += 1; temp = temp->next; }

    temp = head;
    int half = count / 2;
    count = 0;
    while(count < half && temp != nullptr) {
        temp = temp->next;
        count += 1;
    }
    
    return temp;
}