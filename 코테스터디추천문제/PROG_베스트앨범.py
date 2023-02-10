def solution(genres, plays):
    answer = []
    
    dic = {}

    for i in range(len(genres)):
        if genres[i] in dic.keys():
            dic[genres[i]].append((plays[i],i,dic[genres[i]][-1][2] + plays[i]))
        else:
            dic[genres[i]] = [(plays[i],i,plays[i])]
    
    keys = list(dic.keys())
    keys.sort(key = lambda x : dic[x][-1][2],reverse=True)
    print(keys)
    for genre in keys:
        genre_list = dic[genre]
        if len(genre_list)<2:
            answer.append(genre_list[0][1])
        else:
            genre_list.sort(key = lambda x : (-x[0],x[1]))
            print(genre_list)
            top2 = genre_list[:2]
            for top in top2:
                answer.append(top[1])
        print(genre_list)
        
    return answer
    
            
print(solution(["a","b","a"],[5,5,5]))
# answer : [0,2,1]이 되어야함