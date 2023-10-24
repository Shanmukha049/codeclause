import string
import random
#getting our required password length
length=int(input("enter the length of your password:"))
#getting choices of different characters
print("1.Digits\n2.Uppercase Letters\n3.Lowercase Letters\n4.Special Characters\n5.Exit")
characterlist=""
while(True):
  choice=int(input("enter your choices for your password"))
  if(choice==1):
    #adding digits to the password
     characterlist+=string.digits
  elif(choice==2):
    #adding uppercase letters to the password
     characterlist+=string.ascii_uppercase
  elif(choice==3):
     #adding lowercase letters to the password
     characterlist+=string.ascii_lowercase
  elif(choice==4):
     #adding Special Characters to the password
     characterlist+=string.punctuation
  elif(choice==5):
     break
  else:
     print("enter a valid choice")
password=[]
for i in range(length):
   randomcharacter=random.choice(characterlist)
   password.append(randomcharacter)
#finally print your randompassword
print("The random password is:"+"".join(password))

