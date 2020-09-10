class Solution:
    def trap(self, height: List[int]) -> int:
        length=len(height)
        if length==0:
            return 0
        hl=0
        posl=0
        hr=0
        posr=length-1
        ans=0
        for i in range(length):
            if height[i]>=hl:
                ans=ans+(i-posl)*hl
                posl=i
                hl=height[i]
                #print(i,hl,ans,'l')
            if posl>=posr:
                break
            if height[length-i-1]>=hr:
                ans=ans+(posr+i+1-length)*hr
                posr=length-i-1
                hr=height[length-i-1]
                #print(length-i-1,hr,ans,'r')
            if posl>=posr:
                break
        return (ans-sum(height)+max(height))
