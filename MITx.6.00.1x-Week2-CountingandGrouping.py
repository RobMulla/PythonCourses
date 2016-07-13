# Problem 3 - counting and grouping
# Write a function called item_order that takes as input a string named order.
# The string contains only words for the items the customer can order separated by one space.
# The function returns a string that counts the number of each item and consolidates
# them in the following order: salad:[# salad] hamburger:[# hambruger] water:[# water]

def item_order(order):
    length = len(order)
    salad = 0
    water = 0
    hamburger = 0
    for x in range(0,length):
        if order[x:x+len('salad')] == 'salad':
            salad += 1
        if order[x:x + len('water')] == 'water':
            water += 1
        if order[x:x + len('hamburger')] == 'hamburger':
            hamburger += 1

    return 'salad:'+str(salad)+' hamburger:'+str(hamburger)+' water:'+str(water)
