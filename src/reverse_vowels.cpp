#include "main.h"
#include <algorithm>
#include <array>
#include <cctype>
#include <utility>

std::string reverseVowels(std::string s) {
	int i = 0, j = s.size() - 1;
	while(i < j) {
		if(isVowel(s[i]) && isVowel(s[j])) {
			std::swap(s[i], s[j]);
			i++; j--;
		} else if(!isVowel(s[i]) && isVowel(s[j])) {
			i++;
		} else {
			j--;
		}
	}
	return s;
}

bool isVowel(char c) {
	c = std::tolower(c);
	std::array<char, 5> vowels = {'a', 'e', 'i', 'o', 'u'};
	return std::find(vowels.begin(), vowels.end(), c) != vowels.end();
}