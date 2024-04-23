class Solution {
    public int[] solution(String myString) {

        String[] myStringList = myString.split("x");
        boolean lastFlag = myString.charAt(myString.length()-1) == 'x' ? true: false;
        int size = lastFlag == true? myStringList.length+1 : myStringList.length;
        int[] answer = new int[size];
        int i=0;
        for(String data: myStringList){
            answer[i] = data.length();
            i+=1;
        }
        if(lastFlag == true){
            answer[size-1] = 0;
        }
        
        
        
        return answer;
    }
}