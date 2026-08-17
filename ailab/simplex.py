def medical_agent(symptoms):

    if "fever" in symptoms and "cough" in symptoms:
        return "Possible Disease: Flu"

    elif "fever" in symptoms and "rash" in symptoms:
        return "Possible Disease: Measles"

    elif "headache" in symptoms and "nausea" in symptoms:
        return "Possible Disease: Migraine"

    elif "cough" in symptoms and "breathing problem" in symptoms:
        return "Possible Disease: Asthma"

    else:
        return "Disease not identified"


print("=== Simple Medical Diagnosis Agent ===")

symptoms = input("Enter symptoms separated by comma: ").lower()
symptoms = [s.strip() for s in symptoms.split(",")]

result = medical_agent(symptoms)

print(result)