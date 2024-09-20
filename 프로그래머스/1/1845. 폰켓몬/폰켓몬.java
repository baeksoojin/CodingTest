import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        // 최댓값이 될 수 있는 가장 큰 수 : n/2
        // set을 통해, key의 개수와 n/2중 큰 수 -> 최댓값
        
        Set<Integer> typeOfMonster = new HashSet<Integer>();
        
        for(int i=0; i<nums.length; i++){
            typeOfMonster.add(nums[i]);
        }
        
        return Math.min(nums.length/2, typeOfMonster.size());
        
    }
}