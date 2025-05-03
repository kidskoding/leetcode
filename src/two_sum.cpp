#include "main.hpp"
#include <map>
#include <utility>

std::vector<int> twoSum(std::vector<int>& nums, int target) {
	std::map<int, int> map;
	for(int i = 0; i < nums.size(); i++) {
		int difference = target - nums[i];
		if(map.find(difference) != map.end()) {
			return {map[difference], i};
		}
		map.insert(std::make_pair(nums[i], i));
	}
	return {};
}