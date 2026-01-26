from collections import defaultdict

def analyze_logs(logs):
    map = defaultdict(list)
    for x in logs:
        arr = x.split(' ')
        arr = [x for x in arr if 'model' in x or 'time' in x]
        
        model = arr[0][arr[0].index('=') + 1:]
        time = arr[1][arr[1].index('=') + 1:arr[1].index('ms')]
        
        map[model].append(int(time))
        
    newMap = {}
    for x in map.keys():
        newMap[x] = sum(map[x]) // len(map[x])
        
    return newMap
        
print(analyze_logs([
  "user1: model=gpt-4 time=200ms",
  "user2: model=gpt-4 time=180ms",
  "user1: model=gpt-3.5 time=300ms",
  "user2: model=gpt-4 time=220ms"
]))

print(analyze_logs(logs = [
  "user1: model=gpt-4 time=200ms",
  "user2: model=gpt-4 time=180ms",
  "user3: model=gpt-3.5 time=300ms"
]))

print(analyze_logs(logs = [
  "user1: model=gpt-3.5 time=100ms",
  "user2: model=gpt-4 time=400ms",
  "user1: model=gpt-3.5 time=300ms",
  "user2: model=gpt-4 time=200ms"
]))

print(analyze_logs(logs = [
  "user1 :  model=gpt-4   time=100ms",
  "user2:model=gpt-4 time=200ms",
  "user3 : model=gpt-3.5 time=300ms"
]))

print(analyze_logs([]))

print(analyze_logs(logs = ["user5:model=gpt-5 time=10ms"]))