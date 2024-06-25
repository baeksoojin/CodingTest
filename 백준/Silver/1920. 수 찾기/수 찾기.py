n = int(input())

a_list = list(map(int, input().split()))
a_list.sort()

m = int(input())


def bst(num):

    start = 0
    end = n-1
    while start<=end:

        mid = (start+end)//2

        if a_list[mid]== num:
            return 1
        
        if num <= a_list[mid]:
            end = mid-1
        else:
            start = mid+1
        
    return 0


m_list = list(map(int, input().split()))
for num in m_list:
    # a_list에서 num을 찾으면 됨
    print(bst(num))
    

