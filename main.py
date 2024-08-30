# Program Name: Lab2.py
# Course: IT1114/Section XXX
# Student Name: Daniel Urdaneta
# Assignment Number: Lab 2
# Due Date: xx/xx/20XX
# Purpose: This program calculates the food costs for a hackathon based on the number of pizza and salad orders.
# It accounts for discounts on large orders and adds a delivery charge to determine the total amount due.
# Specific resources used: Python documentation for syntax and calculations.

def main():
    # Constants for pricing and quantities
    SALAD_COST = 7.99            # Cost per salad
    PIZZA_COST = 15.99           # Cost per whole pizza
    PIZZA_SLICES = 12            # Number of slices per pizza
    SLICES_PER_PERSON = 3         # Slices allocated per person ordering pizza
    DISCOUNT_THRESHOLD_PIZZAS = 10  # Threshold for pizza discount
    DISCOUNT_THRESHOLD_SALADS = 10   # Threshold for salad discount
    DELIVERY_CHARGE_PERCENTAGE = 0.07 # Delivery charge percentage
    MIN_DELIVERY_CHARGE = 20.00     # Minimum delivery charge

    # Input: Getting number of pizza and salad orders from the user
    num_pizza_orders = int(input("Enter the number of people who ordered pizza: "))
    num_salad_orders = int(input("Enter the number of people who ordered salad: "))

    # Calculate total slices needed and number of pizzas required
    total_slices_needed = num_pizza_orders * SLICES_PER_PERSON
    num_pizzas_needed = (total_slices_needed + PIZZA_SLICES - 1) // PIZZA_SLICES  # Ceiling division

    # Calculate costs before discounts
    total_pizza_cost = num_pizzas_needed * PIZZA_COST
    total_salad_cost = num_salad_orders * SALAD_COST

    # Calculate discounts if applicable
    pizza_discount = total_pizza_cost * 0.15 if num_pizzas_needed > DISCOUNT_THRESHOLD_PIZZAS else 0
    salad_discount = total_salad_cost * 0.15 if num_salad_orders > DISCOUNT_THRESHOLD_SALADS else 0

    # Calculate delivery charge based on total before discounts
    total_before_discounts = total_pizza_cost + total_salad_cost
    delivery_charge = max(total_before_discounts * DELIVERY_CHARGE_PERCENTAGE, MIN_DELIVERY_CHARGE)

    # Calculate total amount due after discounts and including delivery charge
    total_discount = pizza_discount + salad_discount
    total_amount_due = total_before_discounts - total_discount + delivery_charge

    # Display results with required output labels
    print(f"Pizzas ordered: {num_pizzas_needed}")
    print(f"Pizza cost: ${total_pizza_cost:.10f}")  # Ensure correct label format
    print(f"Salad cost: ${total_salad_cost:.2f}")    # Ensure correct label format
    print(f"Total: ${total_before_discounts:.10f}")  # Ensure correct label format
    print(f"Discount: ${total_discount:.10f}")        # Ensure correct label format
    print(f"Delivery: ${delivery_charge:.2f}")        # Ensure correct label format
    print(f"Total amount due: ${total_amount_due:.10f}")  # Ensure correct label format

if __name__ == "__main__":
    main()