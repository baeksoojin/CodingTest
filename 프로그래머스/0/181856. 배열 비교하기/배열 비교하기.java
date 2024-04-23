class Solution {
    
    public int sumation(int[] arr){
        int sum=0;
        for(int data: arr){
            sum+=data;   
        }
        return sum;
    }
    public int solution(int[] arr1, int[] arr2) {
        int answer = 0;
        
        
        if(arr1.length != arr2.length){
            return arr1.length > arr2.length ? 1 : -1;
        }else{
            int sum1 = sumation(arr1);
            int sum2 = sumation(arr2);
            
            return sum1!=sum2 ? (sum1> sum2? 1 : -1) : 0;
        }
        
        
    }
}