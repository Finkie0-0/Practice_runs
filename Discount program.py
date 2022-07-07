#Discount program in terms of the number of people
number_of_people = int(input("Number of people: "))
price_per_person = 1500
discount = 0.25
if number_of_people >= 4:
    total_cost = price_per_person * number_of_people
    total_price = total_cost-(total_cost * discount)
else:
    total_cost = price_per_person * number_of_people
    total_price = total_cost

print(f"The number of people {number_of_people}, and the totaled price is ${total_price}")