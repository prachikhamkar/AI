class SymptomChecker:
    def __init__(self):
        self.symptoms = {
            'fever': ['high temperature', 'chills', 'sweating'],
            'headache': ['pain', 'throbbing', 'pressure'],
            'cough': ['dry cough', 'wet cough', 'persistent cough'],
            'fatigue': ['tiredness', 'low energy', 'weakness'],
            # Add more symptoms and their associated keywords here
        }
    def check_symptoms(self, user_input):
        matched_symptoms = []
        for symptom, keywords in self.symptoms.items():
            for keyword in keywords:
                if keyword in user_input:
                    matched_symptoms.append(symptom)
                    break
        return matched_symptoms

# Example usage
checker = SymptomChecker()
user_input = input("Enter your symptoms: ")
matched_symptoms = checker.check_symptoms(user_input)

if matched_symptoms:
    print("Possible conditions based on your symptoms:")
    for symptom in matched_symptoms:
        print(symptom)
else:
    print("No matching symptoms found.")
