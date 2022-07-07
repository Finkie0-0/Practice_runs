user_name = input("Name: ")
length_max = 20

if len(user_name) > length_max:
    print("User name is too long!")
else:
    print(f"Welcome {user_name}")
