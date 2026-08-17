import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("scores.csv")

X = data[['Hours']]
y = data['Scores']

model = LinearRegression()
model.fit(X, y)

prediction = model.predict(pd.DataFrame({'Hours': [11]}))

print("Predicted score for 11 hours:", prediction[0])