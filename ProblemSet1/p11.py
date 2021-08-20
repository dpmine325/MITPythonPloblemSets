
s = 'azcbobobegghakl' #remove this line
vowel = "aeiou"
count=0

for letter in s:
    for v in vowel:
        if letter == v:
            count +=1
            break
        
print (count)
    
