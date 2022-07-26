class Solution():
    def gcd(self,a,b):
        if b==0:
            return a
        return self.gcd(b,a%b)
    def two_water_jug(self,m,n,d):
        fromjug=m
        tojug=0
        step=1
        while fromjug!=d and tojug!=d:
            temp=min(fromjug,n-tojug)
            fromjug=fromjug-temp
            tojug=tojug+temp
            step+=1
            if fromjug==d or tojug==d:
                break
            if fromjug==0:
                fromjug=m
                step+=1
            if tojug==n:
                tojug=0
                step+=1
        return step
    def fun(self,m,n,d):
        if self.gcd(m,n)!=1:
            return "no solution"
        return self.two_water_jug(m,n,d)
        #return min(two_water_jug(m,n,d),two_water_jug(n,m,d))
sol=Solution()
ans=sol.fun(5,3,4)
print(ans)