#ifndef LIST_NODE_HPP 
#define LIST_NODE_HPP

#include <cstddef>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

#endif // LIST_NODE_HPP