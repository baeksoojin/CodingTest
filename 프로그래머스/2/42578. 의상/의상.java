import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        // 각 종류별로 hash에 저장. 각 종류별 의상 개수를 구하고 나올 수 있는 조합을 구하면 됨.
        
        // 1. 종류별 Hash에 저장
        HashMap<String, ArrayList<String>> clothHashMap = new HashMap<>();
        
        for (String[] cloth : clothes) {
            // 종류별로 리스트를 관리하고, 없으면 새로 ArrayList를 생성하여 추가
            clothHashMap.computeIfAbsent(cloth[1], k -> new ArrayList<>()).add(cloth[0]);
        }
        
        
        // 2. 경우의 수 계산
        for (String key : clothHashMap.keySet()) {
            // 각 의상 종류별로 (의상 수 + 1) 을 곱함 (해당 종류의 옷을 입지 않는 경우를 고려)
            answer *= (clothHashMap.get(key).size() + 1);
        }
        
        // 3. 모든 종류의 옷을 입지 않는 경우는 제외해야 하므로 최종 결과에서 1을 뺌
        return answer - 1;
        
        
    }
}