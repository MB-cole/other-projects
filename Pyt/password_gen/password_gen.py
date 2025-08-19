import random
import string
running = True

key = string.ascii_letters + string.punctuation + string.digits
password = []

for i in range(13):
    password.append(random.choice(key))
        
password = ''.join(password)
print(password)
running = False
        


