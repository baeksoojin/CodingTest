from collections import deque

def solution(cacheSize, cities):
    answer = 0
    count=0
    
    for i, city in enumerate(cities):
        cities[i] = city.lower()
        
        
    queue = []
    
    if cacheSize == 0:
        return len(cities)*5
    
    for i, city in enumerate(cities):
        
        if len(queue)<cacheSize:
            if i==0:
                queue.append(city)
                count+=5
                continue
            if city in set(queue):
                queue.remove(city)
                queue = [city] + queue 
                count+=1
                print(city, i, count)
                continue
            else:
                queue = [city] + queue
                count+=5
                print(city, i, count)
                continue


        if city in set(queue):
            queue.remove(city)
            queue = [city] + queue
            count+=1
        else:
            queue.pop(-1)
            queue = [city] + queue
            count+=5

    
    
    return count