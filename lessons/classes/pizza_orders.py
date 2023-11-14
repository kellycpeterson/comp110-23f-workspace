"""Instantitating a class."""

from lessons.classes.pizza import Pizza 

my_pizza: Pizza = Pizza ()
# above accesses new pizza (constructor)
# below accesses attributes
my_pizza.size = "large"
my_pizza.toppings = 10
my_pizza.gluten_free = True

# printing out some values 
print("my_pizza: ")
print(my_pizza)

print("Pizza:")
print(Pizza)

print("Size attribute: ")
print(my_pizza.size)

# Sal's pizza. Size: medium, toppings: 5, not GF
sals_pizza: Pizza = Pizza("medium", 5, False)
print(sals_pizza.size)

def price(input_pizza: Pizza) -> float:
    """Calculate price of pizza."""
    if input_pizza.size == "large":
        price: float = 6.25
    else: 
        price: float = 5.00 
    price += .75 * input_pizza.toppings 
    if input_pizza.gluten_free:
        price += 1.00
    return price 

print(sals_pizza.price())
print(my_pizza.price())