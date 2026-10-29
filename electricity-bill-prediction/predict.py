
import joblib
import pandas as pd

model = joblib.load("electricity_model.pkl")

data = [[1, 230, 2, 5, 10, 8]]
features = [
    "Global_reactive_power",
    "Voltage",
    "Global_intensity",
    "Sub_metering_1",
    "Sub_metering_2",
    "Sub_metering_3"
]

X_new = pd.DataFrame(data, columns=features)
prediction = model.predict(X_new)

print("Predicted consumption:", round(prediction[0], 3), "kW")


