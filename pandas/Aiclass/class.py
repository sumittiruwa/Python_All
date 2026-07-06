import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Read dataset
df = pd.read_csv("scores.csv")

print(df.head())

# Data Cleaning
print("\nNull Values Before Cleaning:")
print(df.isnull().sum())

df.dropna(inplace=True)

print("\nNull Values After Cleaning:")
print(df.isnull().sum())

# Check duplicate values
print("\nDuplicate Values:", df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("\nDuplicate Values After Removing:", df.duplicated().sum())

# Feature and Target
X = df[['hours']]      # 2D array
Y = df['scores']

# Data Separation
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=0
)

# Model
model = LinearRegression()
model.fit(X_train, Y_train)

# Prediction
Y_pred = model.predict(X_test)

# Evaluation
print("\nMean Squared Error:", mean_squared_error(Y_test, Y_pred))

# Predict score for 9.25 hours
print("Predicted Score:", model.predict([[9.25]]))