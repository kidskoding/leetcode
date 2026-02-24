def fizzBuzz(n):
    # Loop through all numbers from 1 to n + 1. Python ranges are exclusive at the end, so the last
    # number in the range doesn't count
    for i in range(1, n + 1):
        # 1. First check if n is divisible by 3 and 5
        # 
        #   If we first check if it is divisible by 3 and then 5 (or vice versa), 
        #   then the program will lead to undefined behavior
        #   
        #   By checking for if a number is divisible by 3 and 5 first, we can eliminate those numbers and then
        #   focus on only the numbers that are divisible by either 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            
        # 2. Check if a number is divisible by 3 once we know it is not divisible by both 3 and 5
        elif i % 3 == 0:
            print("Fizz")
            
        # 3. Check if a number is divisible by 3 once we know it is not divisible by both 3 and 5 or only 5
        elif i % 5 == 0:
            print("Buzz")
            
        # 4. If not divisible by either 3, 5, or both, just return the number
        else:
            print(i)