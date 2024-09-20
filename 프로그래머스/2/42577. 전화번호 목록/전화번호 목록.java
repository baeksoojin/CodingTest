import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        
        Arrays.sort(phone_book);
        
        boolean flag = true;
        for(int i=0; i<phone_book.length-1; i++){
            String phone = phone_book[i+1];
            
         
            if(("/"+phone).split(phone_book[i])[0].equals("/")){
                flag = false;
                break;
            }
        }
        
        return flag;
    }
}