def get_total_requests(limit, requests):
    requests = [x for x in requests if x <= limit]
    
    sum = 0
    count = 0
    i = 0
    while i < len(requests):
        sum += requests[i]
        
        if sum > limit:
            break
        
        i += 1
        count += 1
            
    return count
    
print(get_total_requests(100, [30, 40, 50, 10, 20]))
print(get_total_requests(100, [50, 50]))
print(get_total_requests(100, [120, 10, 10]))
print(get_total_requests(200, [50, 50, 50, 50, 10]))
print(get_total_requests(100, []))
print(get_total_requests(1000, [100, 200, 300, 400]))