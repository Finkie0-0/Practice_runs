import random
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
special = "!@#$%&*_+-=?"
number = "1234567890"
len = 10
all = upper + lower + special + number
password ="".join(random.sample(all,len))
print(f"You random password is: {password}")