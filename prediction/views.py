from django.shortcuts import render
from django.http import JsonResponse
from .models import PredictionRecord
from .forms import PredictionForm
import numpy as np
import pickle
import os



# Load trained model and scaler
model_path = os.path.join(os.path.dirname(__file__), "used_car_price_model.pkl")
if os.path.exists(model_path):
    with open(model_path, "rb") as file:
        model = pickle.load(file)
else:
    model = None
    
    
scaler_path = os.path.join(os.path.dirname(__file__), "scaler.pkl")

if os.path.exists(scaler_path):
    with open(scaler_path, "rb") as file:
        scaler = pickle.load(file)
else:
    scaler = None


BRAND_MAPPING = {
    "Acura": 28034.08, "Alfa": 37686.05, "Audi": 39907.43, "BMW": 41072.31,
    "Bentley": 137553.55, "Buick": 20357.67, "Cadillac": 41670.73, "Chevrolet": 36722.74,
    "Chrysler": 13812.79, "Dodge": 34500.54, "Ferrari": 243790.67, "Ford": 36240.88,
    "GMC": 37525.68, "Genesis": 43279.90, "Honda": 21959.03, "Hummer": 19618.06,
    "Hyundai": 18946.88, "INFINITI": 22927.64, "Jaguar": 32362.72, "Jeep": 31099.79,
    "Kia": 28096.42, "Lamborghini": 291233.85, "Land": 55764.06, "Lexus": 35668.52,
    "Lincoln": 28330.88, "MINI": 14157.64, "Maserati": 140582.53, "Mazda": 20011.06,
    "Mercedes-Benz": 52075.77, "Mitsubishi": 17550.65, "Nissan": 25905.12, "Other": 103781.76,
    "Pontiac": 13572.93, "Porsche": 88751.30, "RAM": 43029.16, "Rivian": 93138.18,
    "Rolls-Royce": 370992.73, "Subaru": 21495.16, "Tesla": 48439.47, "Toyota": 30026.00,
    "Volkswagen": 22067.97, "Volvo": 26443.92
}

TRANSMISSION_MAPPING = {
    "Manual": [0, 1],
    "Automatic": [1, 0],
    "Other": [0, 0]
}

FUEL_TYPE_MAPPING = {
    "E85 Flex Fuel": 1,
    "Gasoline": 2,
    "Hybrid": 3,
    "Diesel": 4,
    "Plug-In Hybrid": 5,
    "not supported": 6
}

def predict_price(request):
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            brand_encoded = BRAND_MAPPING.get(data.get("brand"), 0)
            fuel_encoded = FUEL_TYPE_MAPPING.get(data.get("fuel_type", "Gasoline"), 2)
            transmission_one_hot = TRANSMISSION_MAPPING.get(data.get("transmission", "Other"), [0, 0])
            clean_title_encoded = 1 if data.get("clean_title") == "Yes" else 0
            accident_reported = 1 if data.get("accident_history") == "Yes" else 0
            accident_none = 1 if accident_reported == 0 else 0

            engine_size = float(data.get("engine_size", 1))
            horsepower_per_liter = float(data.get("horsepower", 0)) / engine_size if engine_size > 0 else 0
            car_age = 2025 - int(data.get("year", 2000))

            raw_input_data = np.array([
                float(data.get("mileage", 0)), fuel_encoded, clean_title_encoded, brand_encoded,
                car_age, accident_reported, accident_none, transmission_one_hot[0], transmission_one_hot[1], horsepower_per_liter
            ]).reshape(1, -1)

            if scaler:
                feature_indices_to_scale = [0, 4, 9]
                raw_input_data[:, feature_indices_to_scale] = scaler.transform(raw_input_data[:, feature_indices_to_scale])
            else:
                return render(request, "predict.html", {"form": form, "error": "Scaler not loaded properly."})

            if not hasattr(model, "predict"):
                return render(request, "predict.html", {"form": form, "error": "Model not found or invalid."})

            predicted_log_price = model.predict(raw_input_data)[0]
            predicted_price = 10 ** predicted_log_price

            return render(request, "predict.html", {"form": form, "predicted_price": round(predicted_price, 2)})

    else:
        form = PredictionForm()

    return render(request, "predict.html", {"form": form})

def home(request):
    return render(request, "home.html")  # Make sure "home.html" exists in the templates folder
