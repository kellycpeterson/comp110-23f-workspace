"""Defining a class."""

class Pizza:

    #attritbutes. name: type
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, inp_size: str, inp_toppings, inp_gf):
        """my constructor."""
        self.size = inp_size
        self.toppings = inp_toppings
        self.gluten_free = inp_gf
    # size = argument
    # can set all the variables as constants in the constructor

def price(self) -> float:
    """Calculate price of pizza:"""
    if self.size == "large":
        price: float = 6.25
    else: 
        price: float = 5.00 
        price += .75 * self.toppings 
    if self.gluten_free:
        price += 1.00
    return price 