class RuleEngine():
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, result):
        self.rules.append((condition, result))

    def apply_rules(self, input_value):
        for condition, result in self.rules:
            if condition(input_value):
                return result
        return "Default"

engine = RuleEngine()
engine.add_rule(lambda x: x < 12570, "Tax rate - 0%")
engine.add_rule(lambda x: 12571 <= x < 50270, "Tax rate - 20%")
engine.add_rule(lambda x: 50271 <= x < 125140, "Tax Rate - 40%")
engine.add_rule(lambda x: x > 125140, "Tax Rate - 45%")


result = engine.apply_rules(12510)
print(result)
