def get_split_list(str):
    
    result = []
    current = ""    
    for i in range(len(str)):
        if 'a' <= str[i] <='z' or 'A' <= str[i] <= 'Z':
            current += str[i].lower()
        else:
            current = ""
            
        if len(current)==2:
            result.append(current)
            current = current[-1]
    return result


def solution(str1, str2):
    answer = 0
    
    # 1. 영문으로 만들기 & 소문자로 통일
    str1_list = get_split_list(str1)
    str2_list = get_split_list(str2)

    # print(str1_list, str2_list)
    
    str1_set = set(str1_list)
    str2_set = set(str2_list)
    
    inter_set = str1_set & str2_set # 교
    union_set = str1_set | str2_set # 합
    
#     print(inter_set, union_set)
    
    inter_elem_count = 0
    union_elem_count = 0
    
    # 다중 집합 체크
    inter_list = list(inter_set)
    union_list = list(union_set)
    for i in range(len(inter_set)):
        
        inter_elem_count += min(str1_list.count(inter_list[i]), str2_list.count(inter_list[i]))

    for i in range(len(union_set)):

        union_elem_count += max(str1_list.count(union_list[i]), str2_list.count(union_list[i]))
    
    if union_elem_count == 0:
        return 65536
    # print(inter_elem_count, union_elem_count)
    return int((inter_elem_count/union_elem_count ) * 65536) 
        