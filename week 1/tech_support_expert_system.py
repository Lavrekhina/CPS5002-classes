class TechSupportExpertSystem:
    def __init__(self):
        self.__issues = {}
        self.__rules = []

    def add_issue(self, category, description_present):
        self.__issues[category] = description_present

    def add_rule(self, conditions, solution):
        self.__rules.append({"conditions": conditions, "solution": solution})

    def troubleshoot(self):
        for rule in self.__rules:
            conditions_met = all(self.__issues.get(condition, False) for condition in rule["conditions"])

            if conditions_met:
                return f"Suggested Solution: {rule['solution']}"

        return "No specific solution found. Please escalate to technical support."


# Example usage
tech_system = TechSupportExpertSystem()

# Add some common issues reported by customers
tech_system.add_issue("Performance", True)      # e.g., Computer is running slow
tech_system.add_issue("Internet", False)        # e.g., Internet not working
tech_system.add_issue("Startup", False)         # e.g., Computer not booting

# Define troubleshooting rules
tech_system.add_rule(["Performance"], "Clear temporary files and optimise settings.")
tech_system.add_rule(["Internet"], "Check router connections and restart the modem.")
tech_system.add_rule(["Startup"], "Ensure power supply is connected and try safe mode.")

print("Welcome to Tech Support Expert System.")
print("Available categories: Performance, Internet, Startup")

# Ask customer to describe their problem
category = input("Please enter the category of your issue: ")
description = input(f"Briefly describe the problem with {category}: ")

# Record the problem as reported
tech_system.add_issue(category, True)

# Diagnose and print solution
result = tech_system.troubleshoot()
print(result)
