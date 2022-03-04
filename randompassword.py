import random 
platform = input("Which platform ? ")

alphabet = "qwertyuiopasdfghjklzxcvbnm"
Alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers  = "1234567890"
symbol   = "@#*&$"

all      = alphabet + Alphabet + numbers + symbol 
length   = 9
password = "".join(random.sample(all,length))

with open("password.txt" , 'a') as i : 
    i.write(platform + " : " + password + "\n")