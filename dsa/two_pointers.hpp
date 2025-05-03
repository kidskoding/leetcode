#ifndef TWO_POINTERS_HPP
#define TWO_POINTERS_HPP

#include <utility>

// Reverse an array!
void reverse(int arr[], int size) {
	int i = 0, j = size - 1;
	while(i < j) {
		std::swap(arr[i], arr[j]);
		i += 1;
		j -= 1;
	}
}

#endif // TWO_POINTERS_HPP