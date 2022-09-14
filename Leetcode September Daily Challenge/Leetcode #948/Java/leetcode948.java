class Solution {
    public int bagOfTokensScore(int[] tokens, int p) {
        Arrays.sort(tokens);//1
        int l = 0, r = tokens.length - 1;
        int score = 0, maxScore = 0;
        
        while( l <= r){
            if(p >= tokens[l]){//FaceUp
                p -= tokens[l++];
                score++;
                maxScore = Math.max(maxScore, score);
            } 
            else if(score > 0){//FaceDown
                p += tokens[r--];
                score--;
            }
            else{
                break;
            }
        }
        return maxScore;
    }
}
