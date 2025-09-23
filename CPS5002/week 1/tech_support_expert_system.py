class MedicalDiagnosisExpertSystem:
    def __init__(self):
        self.symptoms = {}
        self.__rules = []

    def add_symptom(self, name, present):
        self.symptoms[name] = present

    def add_rule(self, conditions, diagnosis):
        self.rules.append({"issue": conditions, "co": diagnosis})

    def diagnose(self):
        for rule in self.rules:
            conditions_met = all(self.symptoms[condition] for condition in rule["conditions"])

            if conditions_met:
                return f"The patient is diagnosed with: {rule['diagnosis']}"

        return "No specific diagnosis based on the observed symptoms."

# Example Usage:
medical_system = MedicalDiagnosisExpertSystem()
medical_system.add_symptom("fever", True)
medical_system.add_symptom("cough", True)
medical_system.add_symptom("headache", True)

medical_system.add_rule(["fever", "cough", "headache"], "Common Cold")
medical_system.add_rule(["fever", "cough"], "Flu")
medical_system.add_rule(["headache"], "Migraine")

result = medical_system.diagnose()
print(result)
