Name1=input("Enter your Name : ")
wordC=1
letterC=0
for i in Name1 :
    letterC=letterC+1
    if(i==' '):
        wordC=wordC+1
print(wordC)
print(letterC)