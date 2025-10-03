class Game:
    def __init__(self):
        # Fuzzy rules
        self.rules = {
            'attack': [('high_energy', 'close_proximity'), ('high_energy', 'medium_proximity')],
            'defend': [('medium_energy', 'close_proximity'), ('low_energy', 'medium_proximity')],
            'run_away': [('low_energy', 'close_proximity'), ('medium_energy', 'far_proximity')]
        }

        # Membership functions for ambient light level
        self.energy_memberships = {
            'low_energy': lambda x: max(0, 1 - abs(x - 15) / 15) if 0 <= x <= 30 else 0,
            'medium_energy': lambda x: max(0, 1 - abs(x - 50) / 20) if 31 <= x <= 70 else 0,
            'high_energy': lambda x: max(0, 1 - abs(x - 85) / 15) if 71 <= x <= 100 else 0
        }

        # Membership functions for room occupancy
        self.proximity_memberships = {
            'close_proximity': lambda x: max(0, 1 - abs(x - 15) / 15) if 0 <= x <= 30 else 0,
            'medium_proximity': lambda x: max(0, 1 - abs(x - 50) / 20) if 31 <= x <= 70 else 0,
            'far_proximity': lambda x: max(0, 1 - abs(x - 85) / 15) if 71 <= x <= 100 else 0
        }

    def __fuzzify(self, value, memberships):
        # Fuzzification: Calculate membership degrees for each linguistic term
        return {term: func(value) for term, func in memberships.items()}

    def __infer(self, fuzzified_energy, fuzzified_proximity):
        # Inference: Apply rules based on fuzzified values of light level and occupancy
        attack = max(
            min(fuzzified_energy[energy], fuzzified_proximity[proximity])
            for energy, proximity in self.rules['attack']
        )
        defend = max(
            min(fuzzified_energy[energy], fuzzified_proximity[proximity])
            for energy, proximity in self.rules['defend']
        )
        run_away = max(
            min(fuzzified_energy[energy], fuzzified_proximity[proximity])
            for energy, proximity in self.rules['run_away']
        )
        return {'attack': attack, 'defend': defend, 'run_away': run_away}

    def __defuzzify(self, inferred_actions):
        # Defuzzification: Choose the action with the highest membership degree
        return max(inferred_actions, key=inferred_actions.get)

    def decide_action(self, energy, proximity):
        # Fuzzification for ambient light and occupancy
        fuzzified_energy = self.__fuzzify(energy, self.energy_memberships)
        fuzzified_proximity = self.__fuzzify(proximity, self.proximity_memberships)

        # Inference: Apply rules to determine the lighting action
        inferred_actions = self.__infer(fuzzified_energy, fuzzified_proximity)

        # Defuzzification: Choose the final action
        return self.__defuzzify(inferred_actions)


if __name__ == "__main__":
    game_actions = Game()

    # Test different combinations of ambient light and occupancy
    test_cases = [
        (10, 20),
        (50, 10),
        (80, 80),
        (20, 10),
        (30, 70),
        (70, 40)
    ]

    for energy, proximity in test_cases:
        action = game_actions.decide_action(energy, proximity)
        print(f"Energy Level: {energy}, Proximity: {proximity} m -> Action: {action}")
