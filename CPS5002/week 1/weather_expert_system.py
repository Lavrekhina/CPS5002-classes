class WeatherExpertSystem:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, conditions, result):
        self.rules.append((conditions, result))

    def infer(self):
        matched_rules = []
        for conditions, result in self.rules:
            # Only consider rules where all conditions are satisfied
            if all(condition in self.facts for condition in conditions):
                matched_rules.append((len(conditions), result))
        if matched_rules:
            # Return the rule with the most conditions (most specific)
            matched_rules.sort(reverse=True)
            return matched_rules[0][1]
        return "No matching rule found."

# Initialize the expert system
expert_system = WeatherExpertSystem()

# Define rules
expert_system.add_rule(["high_temperature", "low_humidity"], "Comfortable")
expert_system.add_rule(["low_temperature", "wind_speed_high"], "Super Cold, take a scarf")
expert_system.add_rule(["cloudy", "fog"], "Take an umbrella, just in case")
expert_system.add_rule(["high_temperature", "wind_speed_low"], "Hot, don't forget the sunglasses")

print("Enter the current weather facts one by one. Type 'done' when finished.")
print("Valid facts examples: high_temperature, low_temperature, low_humidity, fog, cloudy, wind_speed_high, wind_speed_low")

while True:
    fact = input("Fact: ").strip().lower()
    if fact == "done":
        break
    expert_system.add_fact(fact)

result = expert_system.infer()
print("Weather advice:", result)