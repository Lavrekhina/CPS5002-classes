class TechSupportExpertSystem:
    def __init__(self):
        self.user_reports = {}
        self.rules = []

    def report_issue(self, category, description):
        self.user_reports[category] = description

    def add_rule(self, conditions, solution):
        self.rules.append({"conditions": conditions, "solution": solution})

    def troubleshoot(self, category):
        for rule in self.rules:
            if category in rule["conditions"]:
                if self.user_reports.get(category):
                    return f"Suggested solution for {category}: {rule['solution']}"
        return "No specific solution found for the reported issue."


# Пример использования
tech_support_system = TechSupportExpertSystem()

tech_support_system.add_rule(["Performance"], "Clear temporary files and optimize settings.")
tech_support_system.add_rule(["Internet"], "Check network cables and restart the router.")
tech_support_system.add_rule(["Startup"], "Ensure power supply is connected and try safe mode.")

print("Welcome to Tech Support Expert System.")
print("Available categories: Performance, Connectivity, Startup")

category = input("Please select the category of your issue: ")
description = input(f"Briefly describe the problem with {category}: ")

tech_support_system.report_issue(category, description)

result = tech_support_system.troubleshoot(category)
print(result)
