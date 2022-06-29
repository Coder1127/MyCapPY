def most_frequent(s):
    su=s.upper()
    freq={}
    for i in su:
        keys=freq.keys()
        if i not in keys:
            freq[i]=1
        else:
            freq[i] +=1
    f1=sorted(freq.items(), reverse=True , key=lambda x:x[1])        
    print(f1)
    
a=input("Enter A Word to find frequency of letters: ")
print("The frequency of letters is:")    
print (most_frequent(a))
