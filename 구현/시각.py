n = int(input())

count = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            hms = str(h)+ str(m) + str(s)
            if '3' in hms:
                count +=1

print(count)