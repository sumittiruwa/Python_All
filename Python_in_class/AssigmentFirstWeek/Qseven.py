# 7. Fake AI Prediction Confidence Detector 
# A prediction system outputs a confidence score. 
# ● Input confidence score (float) and prediction label (string). 
# ● Conditions: 
# ○ Confidence ≥ 0.9 → “Highly Reliable” 
# ○ 0.7–0.89 → “Moderately Reliable” 
# ○ Below 0.7 → “Unreliable Prediction” 
# ● Also check: 
# ○ If label is empty → “Invalid Prediction”


confidence_score = float(input("Enter confidence score (0 to 1): "))
prediction_label = input("Enter prediction label: ")

if not prediction_label:
    print("Invalid Prediction")
elif confidence_score >= 0.9:
    print("Highly Reliable")
elif 0.7 <= confidence_score < 0.9:
    print("Moderately Reliable")
else:
    print("Unreliable Prediction")

