# Does Calculations for a supermarket pricing

prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
    
total = 0
for fruit in prices:
    total = total + (prices[fruit] * stock[fruit])
    
print total

# Stocking out portion of the project

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# My code
def compute_bill(food):
    total = 0
    for thing in food:
        if stock[thing] > 0:
            total += prices[thing]
            stock[thing] = stock[thing] - 1
    return total
