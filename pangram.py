sentence=input("Enter a sentence.")
alphabet="qwertyuiopasdfghjklzxcvbnm"
for i in alphabet:
 if i not in sentence.lower():
  print("This is not a pangram.")
  break
else: 
   print("This is a pangram") 

 