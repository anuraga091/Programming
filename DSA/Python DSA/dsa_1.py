""" Question is 
A person can eat samosa or pepsi or both. (hint: samosa/pepsi can either be true or false)
There is a discount system on age
If age of the person is less than 9 years then person will get 20% discount
or if age of the person is more than 59 years then person will get 30% discount.
Calculate the cost

cost of samosa = 20
cost of pepsi = 30
"""

#Solution 
pepsi = True;
samosa = True;
age = 61
cost = 0;
if pepsi:
    cost += 30
if samosa:
    cost += 20
if age < 9:
    cost = cost*0.8
elif age > 59:
    cost = cost *0.7
else:
    cost
    
print("Pay", cost, "rupees")
