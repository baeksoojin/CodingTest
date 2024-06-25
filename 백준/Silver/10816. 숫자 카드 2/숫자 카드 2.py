n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()


def bst_first(target):

    start = 0
    end = n-1
    first = -1

    while start<=end:

        mid = (start + end)//2

        if n_list[mid] == target:
            first = mid
            end = mid-1
        elif n_list[mid] >= target:
            end = mid -1
        else:
            start = mid +1

    return first

def bst_last(target):

    start = 0
    end = n-1
    last = -1

    while start<=end:

        mid = (start + end)//2

        if n_list[mid] == target:
            last = mid
            start = mid+1
        elif n_list[mid] >= target:
            end = mid -1
        else:
            start = mid +1

    return last


for num in m_list:

    first = bst_first(num)
    if first == -1:
        print(0, end = " ")
        continue
    last = bst_last(num)
    print(last-first+1, end = " " )
