class DiscountEligibilitySystem:
    def __init__(self):
        self.purchase_history = {}
        self.rules = []

    def add_purchase(self, item, price):
        if item in self.purchase_history:
            self.purchase_history[item] += price
        else:
            self.purchase_history[item] = price

    def add_rule(self, goal, condition_amount):
        self.rules.append({"goal": goal, "conditions": condition_amount})

    def check_discount_eligibility(self, goal):
        total_purchase_amount = sum(self.purchase_history.values())

        if total_purchase_amount == 0:
            return "Customer has no purchase history for evaluation."

        for rule in self.rules:
            if rule["goal"] == goal and total_purchase_amount >= rule["conditions"]:
                return f"The customer is eligible for a {goal} discount. Conditions met: {rule['conditions']}"

        return f"The customer is not eligible for a {goal} discount based on their purchase history."

# Example Usage:
discount_system = DiscountEligibilitySystem()

# Add purchase history
discount_system.add_purchase("Electronics", 800)
discount_system.add_purchase("Clothing", 150)
discount_system.add_purchase("Books", 50)

# Define rules for discount eligibility based on overall purchase amount
discount_system.add_rule("10% Off Electronics", 500)
discount_system.add_rule("20% Off ", 100)

# Check discount eligibility
result = discount_system.check_discount_eligibility("10% Off Electronics")
print(result)