# 2. AI Model Accuracy Comparator 
# Write a Python program that: 
# ● Accepts accuracy values of three ML models (float values). 
# ● Uses comparison and logical operators to: 
# ○ Find the best model 
# ○ Check if all models exceed 90% 
# ○ Check if any model is below 70% 
# ● Print appropriate recommendations. 

model1 = float(input("Enter the accuracy of Model 1: "))
model2 = float(input("Enter the accuracy of Model 2: "))   
model3 = float(input("Enter the accuracy of Model 3: "))

if model1 > model2 and model1 > model3:
    best_model = "Model 1"
elif model2 > model1 and model2 > model3:
    best_model = "Model 2"
else:
    best_model = "Model 3"

all_exceed_90 = model1 > 90 and model2 > 90 and model3 > 90
any_below_70 = model1 < 70 or model2 < 70 or model3 < 70
print(f"The best model is: {best_model}")
if all_exceed_90:
    print("All models exceed 90% accuracy. Great performance!") 