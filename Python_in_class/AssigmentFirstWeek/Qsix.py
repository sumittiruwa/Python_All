# 6. University Grading & AI Recommendation System 
# Create a grading system: 
# ● Input marks for Python, Statistics, and Machine Learning. 
# ● Calculate average. 
# ● Assign grades using if-elif-else. 
# ● Additionally: 
# ○ If average > 85 → Recommend “AI Engineer” 
# ○ If average > 70 → Recommend “Data Analyst” 
# ○ Else → Recommend “Software Developer” 

Python = int(input("Enter marks for Python: "))
Statistics = int(input("Enter marks for Statistics: "))
Machine_Learning = int(input("Enter marks for Machine Learning: "))

averege = (Python + Statistics + Machine_Learning) / 3

if averege > 85:
    print("Grade: A")
    print("Recommendation: AI Engineer")
elif averege > 70:
    print("Grade: B")
    print("Recommendation: Data Analyst")
else:
    print("Grade: C")
    print("Recommendation: Software Developer")    