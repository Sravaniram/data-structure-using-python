n,m=map(int,input().split())
#genaral algorithm time complexcity O(max(m,n))
#def gcd(n,m):
#    for x in range(min(n,m),0,-1):
#       if(n%x==0):
#          if(m%x==0):
#                break
#    return x
#g=gcd(m,n)
#print(g)
#eclude's algorithm for gcd worst algorithm time complexcity O(max(m,n)/2)
#def egcd(n,m):
#    #assining n as gratest among n,m
#    if(n<m):
#        (n,m)=(m,n)
#    if(n%m==0):
#        return(m)
#   else:
#      diff=n-m
#       return(egcd(max(diff,m),min(diff,m)))
#g=egcd(n,m)
#print(g)
#eclude's advanced algorithm for gcd time complexcity is O(min(m,n))
def eagcd(n,m):
    if(n<m):
        (n,m)=(m,n)
    if(n%m==0):
        return m
    else:
        return eagcd(m,n%m)
g=eagcd(n,m)
print(g)

    
