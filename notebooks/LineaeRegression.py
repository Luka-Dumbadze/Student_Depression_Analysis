import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# Load the data
data = pd.read_csv(r'C:\Users\KiuStudnet\PycharmProjects\Student_Depression_Analysis\data\processed_v2_eda_student_depression.csv')
data.dropna(inplace=True)

# Preprocessing
categorical_columns = ['Gender', 'City', 'Profession', 'Dietary Habits', 'Degree', 'Have you ever had suicidal thoughts ?',
                       'Family History of Mental Illness']
encoder = LabelEncoder()
for col in categorical_columns:
    data[col] = encoder.fit_transform(data[col])

# Define features and target
X = data[['Age', 'Academic Pressure', 'Work Pressure', 'CGPA', 'Study Satisfaction',
          'Job Satisfaction', 'Sleep Duration', 'Dietary Habits', 'Work/Study Hours',
          'Financial Stress', 'Family History of Mental Illness']]
y = data['Depression']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and fit the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error (MSE):", mse)
print("R-squared (R2) Score:", r2)

# Visualization
# 1. Target Distribution
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='Depression', palette='coolwarm')
plt.title("Distribution of Depression")
plt.xlabel("Depression")
plt.ylabel("Count")
plt.show()

# 2. Pairplot for Key Features
selected_features = ['Age', 'CGPA', 'Sleep Duration', 'Work/Study Hours', 'Depression']
sns.pairplot(data[selected_features], hue='Depression', palette='coolwarm')
plt.suptitle("Pairplot of Key Features", y=1.02)
plt.show()

# 3. Correlation Heatmap
plt.figure(figsize=(10, 8))
corr = data.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

# 4. Actual vs Predicted
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color='b')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', linewidth=2)
plt.title("Actual vs Predicted Depression")
plt.xlabel("Actual Depression")
plt.ylabel("Predicted Depression")
plt.show()

# 5. Residual Plot
residuals = y_test - y_pred
plt.figure(figsize=(8, 6))
sns.residplot(x=y_pred, y=residuals, lowess=True, color='purple', line_kws={'color': 'red'})
plt.title("Residual Plot")
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.show()
