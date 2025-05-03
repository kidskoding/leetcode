#include "main.hpp"
#include <iostream>

int main(int argc, char** argv) {
    ListNode* node1 = new ListNode(1);
    ListNode* node2 = new ListNode(2);
    ListNode* node3 = new ListNode(3);
    ListNode* node4 = new ListNode(4);
    ListNode* node5 = new ListNode(5);
    
    // Connect nodes to form a linked list
    node1->next = node2;
    node2->next = node3;
    node3->next = node4;
    node4->next = node5;

    isPalindrome(node1);
}
