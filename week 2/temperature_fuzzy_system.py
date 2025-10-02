class FuzzySystem:
    def __init__(self):
        # Rules list
        self.__rules = {
            'fan_on':['very hot', 'hot', 'warm'],
            'heater_on': ['very cold', 'cold']
        }

        # Linguistic terms and membership functions
        self.__memberships = {
            'very_cold': lambda x: max(0, 1 -abs(x-0) / 10),
            'cold': lambda x: max(0, 1 -abs(x-10) / 10),
            'warm': lambda x: max(0, 1 -abs(x-20) / 10),
            'hot': lambda x: max(0, 1 -abs(x-30) / 10),
            'very_hot': lambda x: max(0, 1 -abs(x-40) / 10)
        }

    def __fuzzify(self, temp_value):
        # Fuzzification: Calculate membership degrees for linguistic terms
        return {
            'very_cold': self.__memberships['very_cold'](temp_value),
            'cold': self.__memberships['cold'](temp_value),
            'warm': self.__memberships['warm'](temp_value),
            'hot': self.__memberships['hot'](temp_value),
            'very_hot': self.__memberships['very_hot'](temp_value)
        }

    def __inference(self, antecedents):
        # Rule Evaluation: Apply rules to determine the consequent
        return {
            'fan_on': antecedents['hot'] + antecedents['very_hot']+antecedents['warm'],
            'heater_on': antecedents['very_cold'] + antecedents['cold']
        }

    def __defuzzify(self, consequents):
        # Defuzzification: Choose the consequent with the highest aggregated degree of membership
        if consequents['fan_on'] < consequents['heater_on']:
            return 'Heter On'
        elif consequents['fan_on'] > consequents['heater_on']:
            return 'Fan On'
        else:
            return 'Off'

    def evaluate(self, temperature):
        # Fuzzification for input temperature
        fuzzified_values = self.__fuzzify(temperature)

        # Inference: Apply rules to determine the fan/heater operation
        inference_result = self.__inference(fuzzified_values)

        # Defuzzification: Choose the final system operation
        return self.__defuzzify(inference_result)


if __name__ == "__main__":
    fuzzy_system = FuzzySystem()

    # Test different temperature values
    test_temperatures = [-5, 5, 15, 25, 35, 45]

    for temp in test_temperatures:
        result = fuzzy_system.evaluate(temp)
        print(f"Temperature: {temp}°C -> System: {result}")