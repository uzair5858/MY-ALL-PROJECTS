import pandas as pd

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# ==========================================
# 1. LOAD DATASET
# ==========================================

data = fetch_california_housing()

# Dataset ko DataFrame mein convert kar rahe hain
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target


# Model ko features ka correct order
feature_order = [
    "MedInc",
    "HouseAge",
    "AveRooms",
    "AveBedrms",
    "Population",
    "AveOccup",
    "Latitude",
    "Longitude"
]


# ==========================================
# 2. SPLIT DATA
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================
# 3. CREATE MODEL
# ==========================================

model = LinearRegression()


# ==========================================
# 4. TRAIN MODEL
# ==========================================

model.fit(X_train, y_train)


# ==========================================
# 5. TEST MODEL
# ==========================================

y_pred = model.predict(X_test)


# ==========================================
# 6. EVALUATE MODEL
# ==========================================

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n==============================")
print("MODEL TRAINING COMPLETE ✅")
print("==============================")

print("Mean Squared Error:", mse)
print("R² Score:", r2)


# ==========================================
# 7. LOAD NEW DATA
# ==========================================

print("\n==============================")
print("READING NEW DATA")
print("==============================")

try:
    new_df = pd.read_csv("new_data.csv")

except FileNotFoundError:
    print("❌ new_data.csv file nahi mili.")
    print("Please new_data.csv ko main.py ke same folder mein rakho.")
    exit()

except Exception as e:
    print("❌ CSV read karne mein error:", e)
    exit()


# ==========================================
# 8. CHECK REQUIRED FEATURES
# ==========================================

missing_features = [
    feature
    for feature in feature_order
    if feature not in new_df.columns
]

if missing_features:

    print("\n❌ Kuch features missing hain:")

    for feature in missing_features:
        print("-", feature)

    print("\nPrediction nahi ho sakti.")
    exit()


# ==========================================
# 9. SELECT FEATURES
# ==========================================

try:

    # Columns ka order automatically correct hoga
    new_data = new_df[feature_order]

except Exception as e:

    print("❌ Data arrange karne mein error:", e)
    exit()


# ==========================================
# 10. CHECK MISSING VALUES
# ==========================================

if new_data.isnull().any().any():

    print("\n? New data mein missing value hai.")

    for column in new_data.columns:

        missing_rows = new_data[column].isnull()

        for row_number in new_data.index[missing_rows]:

            print(
                f"Row {row_number + 1}: "
                f"{column} ki value missing hai."
            )

    print("\nPrediction nahi ho sakti.")
    exit()


# ==========================================
# 11. CHECK NUMERIC DATA
# ==========================================

try:

    new_data = new_data.apply(pd.to_numeric)

except Exception:

    print("\n? New data mein koi value number nahi hai.")
    print("Please sirf numeric values use karo.")
    exit()

# ==========================================
# 12. MAKE PREDICTIONS
# ==========================================

new_predictions = model.predict(new_data)


# ==========================================
# 13. SHOW PREDICTIONS
# ==========================================

print("\n==============================")
print("NEW DATA PREDICTIONS")
print("==============================")

for i, prediction in enumerate(new_predictions, start=1):

    print(f"Row {i}: {prediction:.4f}")


# ==========================================
# 14. SAVE PREDICTIONS
# ==========================================

result = new_df.copy()

result["Predicted_House_Value"] = new_predictions

result.to_csv("predictions.csv", index=False)


print("\n==============================")
print("PROJECT COMPLETE ✅")
print("==============================")

print("Predictions save ho gayi hain:")
print("predictions.csv")


