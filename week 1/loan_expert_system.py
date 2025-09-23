class LoanEligibilitySystem:
    def __init__(self):
        self.facts = {}
        self.rules = []

    def add_fact(self, fact_type, value):
        self.facts[fact_type] = value

    def add_rule(self, goal, conditions):
        self.rules.append({"goal": goal, "conditions": conditions})

    def check_loan_eligibility(self, goal):
        if not all(self.facts.values()):
            return "Incomplete financial information for evaluation."

        for rule in self.rules:
            if rule["goal"] == goal:
                conditions_met = all(self.facts[condition] >= threshold for condition, threshold in rule["conditions"].items())

                if conditions_met:
                    return f"The individual is eligible for a {goal} loan."

        return f"The individual is not eligible for a {goal} loan based on their financial situation."


# Example Usage:
loan_system = LoanEligibilitySystem()

# Add facts for individual's income and credit score
loan_system.add_fact("income", 50000)
loan_system.add_fact("credit_score", 500)

# Define rules for loan eligibility
loan_system.add_rule("Mortgage", {"income": 50000, "credit_score": 650})
loan_system.add_rule("Personal", {"income": 30000, "credit_score": 600})

# Check mortgage loan eligibility
print(loan_system.check_loan_eligibility("Mortgage"))