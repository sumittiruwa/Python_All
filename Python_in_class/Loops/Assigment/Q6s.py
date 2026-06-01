# 6. AI Prediction Filter Using Lambda 
# A machine learning model generates confidence scores: 
# scores = [0.45, 0.92, 0.88, 0.65, 0.99, 0.71] 
# Write a program that filters predictions having confidence greater than 0.80. 
# Requirements: 
# ● Use filter(). 
# ● Use a lambda function. 
# ● Display all filtered confidence scores.
 
scores = [0.45, 0.92, 0.88, 0.65, 0.99, 0.71]

filtered_scores = list(filter(lambda score: score > 0.80, scores))

print("Filtered Confidence Scores:", filtered_scores)