# -*- coding: utf-8 -*-
"""Task 2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a0pepZQeB5WruYxMWNrNdAMTvgz1ZaLY
"""

import pandas as pd

df = pd.read_csv("/content/real_estate_dataset - Copy.csv")
df.head(150)

df.info()
df.isnull().sum()
df.describe()

df = df.dropna()

import seaborn as sns
import matplotlib.pyplot as plt

df.hist(figsize=(15, 10))
plt.tight_layout()
plt.show()

sns.pairplot(df)
plt.show()

sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()

print(df.columns)

X = df.drop(columns=["Price"])
y = df["Price"]

print(df.columns)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


X = df.drop(columns=["Price"])
y = df["Price"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("MSE:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

freq_table = df["Num_Bedrooms"].value_counts()
print(freq_table)

sns.countplot(x="Num_Bedrooms", data=df)
plt.title("Bedrooms Distribution")
plt.xlabel("Num of Bedrooms")
plt.ylabel("Num of Houses")
plt.show()

df["Num_Bedrooms"].value_counts().plot.pie(
    autopct='%1.1f%%',
    figsize=(6, 6),
    startangle=90
)

plt.title("Percentage of houses by number of bedrooms")
plt.ylabel("")
plt.show()

print(df["Num_Bathrooms"].value_counts())

sns.countplot(x="Num_Bathrooms", data=df)
plt.title("Percentage of houses by number of bathrooms")
plt.xlabel("Num of Bathrooms")
plt.ylabel("Num of Houses")
plt.show()

df["Num_Bathrooms"].value_counts().plot.pie(autopct='%1.1f%%', figsize=(8,8))
plt.title("Percentage of houses by number of bathrooms")
plt.ylabel("Num of Houses")
plt.show()

print(df["Num_Floors"].value_counts())

sns.countplot(x="Num_Floors", data=df)
plt.title("Num of Houses by number of floors")
plt.xlabel("Num of floors")
plt.ylabel("Num of Houses")
plt.show()

df["Num_Floors"].value_counts().plot.pie(autopct='%1.1f%%', figsize=(6,6))
plt.title("Percentages of houses by number of floors")
plt.ylabel("Num of Houses")
plt.show()

print(df["Has_Garden"].value_counts())

sns.countplot(x="Has_Garden", data=df)
plt.title("Houses according to the presence of a garden")
plt.xlabel("Is there a park?")
plt.ylabel("Num of Houses")
plt.show()

df["Has_Garden"].value_counts().plot.pie(autopct='%1.1f%%', figsize=(6,6))
plt.title("The percentage of houses that have garden")
plt.ylabel("Num of Houses")
plt.show()

plt.figure(figsize=(7, 2))
sns.boxplot(x=df[col])
plt.title(f"Boxplot")
 plt.xlabel(col)
plt.show()

import pandas as pd

df = pd.read_csv("/content/real_estate_dataset - Copy.csv")

print(df["Square_Feet"].describe())

import seaborn as sns
import matplotlib.pyplot as plt
sns.histplot(df["Square_Feet"], bins=20, kde=True)
plt.title("Distribution of Houses")
plt.xlabel("Area")
plt.ylabel("Num of Houses")
plt.show()

print(df.dtypes)
print(df.isnull().sum())

X = df.drop(columns=["Price", "ID"])
y = df["Price"]

new_data = pd.DataFrame({
    "Square_Feet": [3000],
    "Num_Bedrooms": [4],
    "Num_Bathrooms": [3],
    "Num_Floors": [3],
    "Year_Built": [2025],
    "Has_Garden": [1],
    "Has_Pool": [0],
    "Garage_Size": [3],
    "Location_Score": [7],
    "Distance_to_Center": [5]
})

predicted_price = model.predict(new_data)
print("The expected price of the property:", predicted_price[0])