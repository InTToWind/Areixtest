class Solution:
    def woodwork(self,satistfaction:List[int])->int:
        s=sorted(satisfaction)
        if len(s)==0:
            return 0
        t=list(range(len(s)+1))[1:(len(s)+1)]
        now=0
        c_s=0
        prefix_sum=[0]
        for i in range(len(s)):
            now=now+s[i]*t[i]
            c_s+=s[i]
            prefix_sum.append(c_s)
        total_sum=sum(s)
        ans=now
        for i in range(len(s)):
            now=now-(total_sum-prefix_sum[i])
            ans=max(ans,now)
        return ans