import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the heart disease dataset (replace 'heart_disease.csv' with your actual file path)
data = pd.read_csv('heart.csv')

# Check for missing values
print("Missing values summary:")
print(data.isnull().sum())

# Handle missing values (e.g., impute or remove rows with missing values)
# ... (your data cleaning logic here)

# Analyze target variable (heart disease) distribution
sns.countplot(x='target', data=data)  # target: 0 (no disease), 1 (disease)
plt.title("Distribution of Heart Disease")
plt.show()

# Explore numerical features (consider using boxplots or histograms for outliers)
numerical_features = ['age', 'trestbps', 'chol', 'fbs', 'thalach', 'oldpeak']
data.boxplot(column=numerical_features)
plt.suptitle('Distribution of Numerical Features')
plt.show()

# Analyze categorical features with respect to target variable
categorical_features = ['sex', 'cp', 'restecg', 'exang', 'slope', 'ca', 'thal']
for feature in categorical_features:
  sns.countplot(x=feature, hue='target', data=data)
  plt.title(f"Distribution of {feature} by Heart Disease")
  plt.show()

# Feature Correlation Analysis (consider using heatmaps)
correlation = data.corr()
fig, ax = plt.subplots(figsize=(4, 4))
sns.heatmap(correlation, annot=True, ax=ax)
plt.title("Correlation Matrix of Features")
plt.show()

# Create a scatter matrix for detailed exploration (Seaborn offers pairplot)
sns.pairplot(data, hue='target')
plt.show()

# Explore features using interactive plots (Plotly)
fig = px.scatter(data, x='age', y='chol', color='target', hover_data=list(data.columns))
fig.update_layout(title='Heart Disease Risk by Age and Cholesterol')
fig.show()
