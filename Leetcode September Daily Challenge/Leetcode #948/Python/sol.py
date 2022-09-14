class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        if not tokens or power<min(tokens):
            return 0
        i=0
        j=len(tokens)-1
        tokens.sort()
        score=0
        while i<=j:
            if tokens[i]<=power:
                score+=1
                power-=tokens[i]
                i+=1
            elif i==j:
                break
            else:
                score-=1
                power+=tokens[j]
                j-=1
        return score
