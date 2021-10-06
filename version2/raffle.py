"""Randomly pick customer and print customer info"""

# Add code starting here
import customers
from random import choice
# Hint: remember to import any functions you need from
# other files or libraries
def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(customers)
    
    name = chosen_customer.name
    email = chosen_customer.email

    print(f"Tell {name} at {email} that they've won")


def run_raffle():
    """Run the weekly raffle."""

    customer = customers.get_customers_from_file("customers.txt")
    pick_winner(customer)

run_raffle()