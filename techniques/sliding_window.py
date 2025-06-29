'''
    Write a function to calculate the maximum number of `fruits` you can collect 
    from an integer array fruits, where each element represents a type of fruit. 
    You can start collecting fruits from any position in the array, 
    but you must stop once you encounter a third distinct type of fruit. 
    The goal is to find the longest subarray where at most two different types of fruits are collected.
    
    Test Case #1:
        Sample Input:
            fruits = [3, 3, 2, 1, 2, 1, 0]
        Sample Output:
            4
        Explanation:
            There are 4 fruits that can be picked up from the subarray [2, 1, 2, 1]
'''

# This is the same Fruits into Basket problem from leetcode. 
# One common problem that utilizes the sliding window technique!
def sliding_window_demo(fruits):
    # start index of the current sliding window
    start = 0

    # tracks the maximum number of fruits collected in a valid window
    max_fruits = 0

    # dictionary to store the count of each fruit type in the current window
    state = {}

    # iterate through the fruit array using the end index of the window
    for end in range(len(fruits)):
        # add the current fruit to the window and update its count
        state[fruits[end]] = state.get(fruits[end], 0) + 1

        # if the window contains more than two fruit types, shrink it from the left
        while len(state) > 2:
            state[fruits[start]] -= 1

            # remove the fruit type from the map if its count drops to zero
            if state[fruits[start]] == 0:
                del state[fruits[start]]

            # move the start of the window forward
            start += 1

        # update the maximum window size found so far
        max_fruits = max(max_fruits, end - start + 1)

    # return the length of the longest valid subarray
    return max_fruits
