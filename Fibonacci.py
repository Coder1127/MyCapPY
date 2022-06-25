n=int(input("Enter no. of terms"))

t1=0
t2=1

if n==0:
    print("No. of Terms should be +ve")
elif n==1:
    print(t1,t2)

else:
    print(t1)
    print(t2)
    for i in range(2,n+1):
        nt=t1+t2
        print(nt)
        t1=t2
        t2=nt
        i +=1
