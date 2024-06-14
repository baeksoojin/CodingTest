from typing import Counter


N = int(input())

def dfs(word,wdict):
    # 종료 조건
    if len(word) == len(words):
        print(word)
        return

    for w in wdict.keys():
        if wdict[w]:
            wdict[w] -= 1
            dfs(word+w, wdict)
            wdict[w] += 1

for i in range(N):
    words = sorted(list(input().strip()))

    # 중복 체크를 위한 dict
    word_dict = dict(Counter(words))
    dfs('',word_dict)
