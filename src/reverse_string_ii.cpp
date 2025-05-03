#include "reverse_string_ii.hpp"
#include "main.hpp"
#include <utility>

std::string reverseStr(std::string& s, int k) {
	std::string result;
	int count = 0;
	for(int i = 0; i < s.size(); i += k) {
		if(count % 2 == 0) { result += helper(s.substr(i, k)); }
		else { result += s.substr(i, k); }
		count += 1;
	}
	return result;
}

std::string helper(std::string s) {
	int left = 0, right = s.size() - 1;
	while(left < right) {
		std::swap(s[left], s[right]);
		left += 1; right -= 1;
	}
	return s;
}