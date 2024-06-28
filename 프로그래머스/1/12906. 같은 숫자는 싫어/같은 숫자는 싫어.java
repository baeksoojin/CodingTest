import java.util.*;

public class Solution {
    public Stack<Integer> solution(int []arr) {
        
        Stack<Integer> stack = new Stack();
        
        // stack -> push, pop
        
        for(int i=0; i<arr.length; i++){
            // stack이 비었을 땐 그냥 넣음
            if(stack.empty() || stack.peek() != arr[i]){
                stack.push(arr[i]);
            }
            
        }
        
//         int[] result = new int[stack.size()];
//         for(int i=0; i<result.length; i++){
//             result[result.length - i-1] = stack.pop();
//         }
        
        return stack;
    }
}