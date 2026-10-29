
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Load dataset
df = pd.read_csv(
    "household_power_consumption.txt",
    sep=";", na_values=["?"], decimal=",", nrows=10000
)

# 2. Select features and target
features = [
    "Global_reactive_power", "Voltage", "Global_intensity",
    "Sub_metering_1", "Sub_metering_2", "Sub_metering_3"
]
target = "Global_active_power"

# 3. Clean data
df[features + [target]] = df[features + [target]].apply(
    pd.to_numeric, errors="coerce"
)
df = df.dropna(subset=features + [target])

X = df[features]
y = df[target]

# 4. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Train model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Predict and evaluate
y_pred = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# 7. Save model
joblib.dump(model, "electricity_model.pkl")
print("Model saved successfully!")

