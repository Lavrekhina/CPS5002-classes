class FuzzySystem:
    def __init__(self):
        # Rules list
        self.rules = {
            # TODO: Write code here
            # E.g., 'fan_on': ['hot', 'very_hot']
        }

        # Linguistic terms and membership functions
        self.memberships = {
            # TODO: Write code here
            # E.g., 'very_cold': lambda x: max(0, 1 - abs(x - 0) / 10)
        }

    def __fuzzify(self, temp_value):
        # Fuzzification: Calculate membership degrees for linguistic terms
        # TODO: write code here

    def __infer(self, antecedents):
        # Rule Evaluation: Apply rules to determine the consequent
        # TODO: write code here

    def __defuzzify(self, consequent):
        # Defuzzification: Choose the consequent with the highest aggregated degree of membership
        # TODO: write code here

    def evaluate(self, temperature):
        # Fuzzification for input temperature
        # TODO: write code here

        # Inference: Apply rules to determine the consequent
        # TODO: write code here

        # Defuzzification: Choose the final operation
        # TODO: write code here


if __name__ == "__main__":
    # TODO: write code here