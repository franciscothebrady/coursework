## tests with lists in python
## can combine lists of string labels 
# with numeric values 
menu_prices = {"Plain Cheese Pizza": 18.99,
 "Garlic Knots": 6.99,
 "Soda":7.00,
 "Oreo Cookie Shake":10.49,
 "White Pizza":22.25,
 "Mozzarella Sticks":17.99
 }

# can print lists 
print(menu_prices)
# can pull list values with string label
print(menu_prices["Plain Cheese Pizza"])
# can perform math on numeric elements in list
print(menu_prices["Plain Cheese Pizza"]*2)


print(f"Total Cost: {menu_prices['Plain Cheese Pizza']*4}")

print(f"Total Cost: {(menu_prices['Plain Cheese Pizza']*4) + menu_prices['Soda']*2 }")