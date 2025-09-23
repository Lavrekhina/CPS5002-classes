import re

class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, response):
        self.rules.append({"condition": condition, "response": response})

    def apply_rules(self, text):
        for rule in self.rules:
            match = re.search(rule["condition"], text, re.IGNORECASE)
            if match:
                # If there's a capture group, format it into the response
                if match.groups():
                    return f"Bot: {rule['response'].format(*match.groups())}"
                return f"Bot: {rule['response']}"
        return "Bot: I don't understand."


# Initialize the chatbot
rule_engine = RuleEngine()

# Greetings & farewells
rule_engine.add_rule(r'\bhello\b|\bhi\b',
                     "Hi there! I can suggest travel destinations. What's your preferred type of trip?")
rule_engine.add_rule(r'\bgoodbye\b|\bbye\b', "Goodbye! Hope you enjoy your travels!")
rule_engine.add_rule(r'\bthank you\b|\bthanks\b', "You're welcome! Safe travels!")

# Capture name
rule_engine.add_rule(r'\bmy name is (.+?)\b',
                     "Nice to meet you, {0}! What kind of travel experience are you looking for?")

# Travel preference rules
rule_engine.add_rule(r'\bbeach\b|\bsea\b|\bsun\b', "If you love the beach, you might enjoy Bali, Maldives, or Hawaii!")
rule_engine.add_rule(r'\bcity\b|\burban\b|\bcities\b', "For city trips, try New York, Tokyo, or Paris!")
rule_engine.add_rule(r'\badventure\b|\bhiking\b|\btrekking\b', "For adventure, consider Patagonia, Nepal, or Iceland!")
rule_engine.add_rule(r'\bculture\b|\bhistory\b|\bmuseum\b', "For cultural trips, you might love Rome, Kyoto, or Cairo!")

# Have conversation
while True:
    user_input = input("You: ")
    response = rule_engine.apply_rules(user_input)
    print(response)

    if re.search(r'\bgoodbye\b|\bbye\b', user_input, re.IGNORECASE):
        break