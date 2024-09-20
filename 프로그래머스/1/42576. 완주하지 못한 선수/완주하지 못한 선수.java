import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        // hash -> key : name / value : count
        
        HashMap<String, Integer> participantHash = new HashMap<>();
        
        // 참가자 명단을 HashMap에 저장
        for (String name : participant) {
            participantHash.put(name, participantHash.getOrDefault(name, 0) + 1);
        }
        
        // 완주한 사람들 명단을 이용해 카운트 감소
        for (String name : completion) {
            participantHash.put(name, participantHash.get(name) - 1);
        }
        
         // 완주하지 못한 사람을 찾음
        for (String name : participantHash.keySet()) {
            if (participantHash.get(name) > 0) {
                answer = name;
                break;
            }
        }
        
        return answer;
        
    }
}