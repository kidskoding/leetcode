#ifndef MAIN_HPP
#define MAIN_HPP

#include <string>
#include <vector>
#include "../dsa/list_node.hpp"

std::vector<int> twoSum(std::vector<int>& nums, int target);
std::string reverseVowels(std::string s);
std::vector<int> dailyTemperatures(std::vector<int> temperatures);
std::string reverseStr(std::string& s, int k);

// Linked List stuff
bool hasCycle(ListNode *head);
bool isPalindrome(ListNode *head);
ListNode* swapPairs(ListNode *head);
ListNode* reverseList(ListNode *head);
ListNode* mergeTwoLists(ListNode *list1, ListNode *list2);
ListNode* deleteDuplicates(ListNode *head);
ListNode* removeElements(ListNode *head, int val);

#endif // MAIN_HPP