'''
The first letter compares to second one, 
if first_letter <= second_letter
    assign first 2 letters to tempWord;
    look for next letter;
if first_letter <= second_letter
    assign second letter to tempWord.

More generaized, 
for letter in s:
    
if s[i] <=s[i+1]
    tempWord +=s[i+1]
    
if s[i] > s[i+1]
    tempWord = s[i]
'''


s = 'acblwykxazeehwtgtjgjmk' #remove this line to submit

tempWord = s[0]
finalWord= ''

for i in range (len(s)-1):
    if s[i] <= s[i+1]:
        tempWord+=s[i+1]
        
    else:
        if len (finalWord) < len (tempWord):
            finalWord = tempWord
        tempWord = s[i+1]
        
if len (finalWord) < len (tempWord):
    finalWord = tempWord

    

print ("Longest substring in alphabetical order is: ", finalWord)