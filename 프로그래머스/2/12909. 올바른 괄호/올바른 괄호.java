import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
    
        Stack<Character> stack = new Stack();
        
        for(int i=0; i<s.length(); i++){
            
            if(s.charAt(i) == '('){
                stack.push(s.charAt(i));
            }else{
                if(stack.empty()){ // 없는데 빼면 false
                    return false;
                }else if(stack.peek() != '('){// 있을 때는 직전에 있는 값이 ")"이 아니라면 false
                    return false;
                }else{
                    stack.pop();
                }
            }
            
        }
        
        if(!stack.empty()){
            return false;
        }
        
    
        return answer;
    }
}