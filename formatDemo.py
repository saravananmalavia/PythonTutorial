price = 49
#txt = "The price is {} dollars"
txt = "The price is {:.3f} dollars"
print(txt.format(price))
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

myorder1 = "I have a {carname}, it is a {model}."
print(myorder1.format(carname = "Ford", model = "Mustang"))