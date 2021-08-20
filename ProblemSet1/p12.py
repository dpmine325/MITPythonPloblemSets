s = 'azcbobobegghaklbob' #remove this line
checkString = "bob"
count=0
t=0

while True:
    t=s.find(checkString,t)
    if t == -1:
        break
    count+=1
    t+=1

        
print (count)