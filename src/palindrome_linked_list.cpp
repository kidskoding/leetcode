#include "main.hpp"
#include <iostream>
#include <vector>

bool isPalindrome(ListNode *head) {
    std::vector<int> values;
    ListNode *currNode = head;
    while(currNode != nullptr) {
        values.push_back(currNode->val);
        currNode = currNode->next;
    }

    int left = 0, right = values.size() - 1;
    while(left < right) {
        if(values[left] != values[right]) { return false; } 
        else { left += 1; right -= 1; }
    }

    return true;
}