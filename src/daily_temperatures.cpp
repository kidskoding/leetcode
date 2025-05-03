#include "main.hpp"
#include <stack>
#include <vector>

std::vector<int> dailyTemperatures(std::vector<int> temperatures) {
	std::vector<int> answer(temperatures.size(), 0);
	std::stack<int> stack;
	for(int i = 0; i < temperatures.size(); i++) {
		while(!stack.empty() && temperatures[i] > temperatures[stack.top()]) {
			int index = stack.top();
			stack.pop();
			answer[index] = i - index; 
		}
		stack.push(i);
	}
	return answer;
}