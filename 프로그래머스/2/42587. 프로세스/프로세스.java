import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        Deque<int[]> queue = new LinkedList<>();
        List<Integer> answerTemp = new ArrayList<>();
        
        // queue 초기화
        for (int i = 0; i < priorities.length; i++) {
            queue.offer(new int[]{i, priorities[i]});
        }
        
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int curLoc = current[0];
            int curPri = current[1];
            
            boolean isPrint = true;
            
            // 뒤에 더 높은 우선순위가 있는지 확인
            for (int[] item : queue) {
                if (item[1] > curPri) {
                    isPrint = false;
                    queue.offer(current); // 다시 큐에 넣음
                    break;
                }
            }
            
            if (isPrint) {
                answerTemp.add(curLoc);
            }
        }
        
        // location에 해당하는 인덱스 찾기
        for (int i = 0; i < answerTemp.size(); i++) {
            if (answerTemp.get(i) == location) {
                answer = i + 1; // 1부터 시작하므로 +1
                break;
            }
        }
        
        return answer;
    }
}
