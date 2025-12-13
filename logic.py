a,b,c=100,100,100
dict={500:a,200:b,100:c}
target=int(input())

def expand(target):
    l=[]
    i=0
    while target>0:
        b=target%10
        c=b*(10**i)
        if c!=0 :
            l.append(c)
        target=target//10
        i+=1
    return l

def despensing(x): 
    for i in dict:
        count=0
        if x%i==0:
            count+=1
        