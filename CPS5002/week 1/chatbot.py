class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, response):
        self.rules.append({"condition": condition, "response": response})

    def apply_rules(self, text):
        for rule in self.rules:
            if rule["condition"] in text.lower():
                return f"Bot: {rule['response']}"
        return "Bot: I don't understand."


# Example usage
rule_engine = RuleEngine()

# Add general rules
rule_engine.add_rule("hello", "Hi there! I can recommend movies. What genre are you interested in?")
rule_engine.add_rule("hi", "Hello! Want me to suggest some movies?")
rule_engine.add_rule("goodbye", "Goodbye! Enjoy your movie night!")

# Add movie recommendation rules by genre
rule_engine.add_rule("action", "If you like action, I recommend: *Mad Max: Fury Road*, *John Wick*, or *Die Hard*.")
rule_engine.add_rule("comedy", "For comedy, you might enjoy: *Superbad*, *The Hangover*, or *Step Brothers*.")
rule_engine.add_rule("drama", "For drama, check out: *The Shawshank Redemption*, *Forrest Gump*, or *The Godfather*.")
rule_engine.add_rule("romance", "For romance, you could watch: *Pride & Prejudice*, *La La Land*, or *The Notebook*.")
rule_engine.add_rule("sci-fi", "If you like sci-fi, try: *Inception*, *The Matrix*, or *Interstellar*.")
rule_engine.add_rule("horror", "For horror fans: *The Conjuring*, *Hereditary*, or *A Quiet Place*.")

# Have conversation
while True:
    user_input = input("You: ")
    response = rule_engine.apply_rules(user_input)
    print(response)

    if user_input.lower() == "goodbye":
        break