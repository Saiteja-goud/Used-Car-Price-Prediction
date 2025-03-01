from django import forms

# Mapping of brand names to their encoded numerical values
BRAND_CHOICES = [
    ("Acura", "Acura"),
    ("Alfa", "Alfa"),
    ("Audi", "Audi"),
    ("BMW", "BMW"),
    ("Bentley", "Bentley"),
    ("Buick", "Buick"),
    ("Cadillac", "Cadillac"),
    ("Chevrolet", "Chevrolet"),
    ("Chrysler", "Chrysler"),
    ("Dodge", "Dodge"),
    ("Ferrari", "Ferrari"),
    ("Ford", "Ford"),
    ("GMC", "GMC"),
    ("Genesis", "Genesis"),
    ("Honda", "Honda"),
    ("Hummer", "Hummer"),
    ("Hyundai", "Hyundai"),
    ("INFINITI", "INFINITI"),
    ("Jaguar", "Jaguar"),
    ("Jeep", "Jeep"),
    ("Kia", "Kia"),
    ("Lamborghini", "Lamborghini"),
    ("Land", "Land"),
    ("Lexus", "Lexus"),
    ("Lincoln", "Lincoln"),
    ("MINI", "MINI"),
    ("Maserati", "Maserati"),
    ("Mazda", "Mazda"),
    ("Mercedes-Benz", "Mercedes-Benz"),
    ("Mitsubishi", "Mitsubishi"),
    ("Nissan", "Nissan"),
    ("Other", "Other"),
    ("Pontiac", "Pontiac"),
    ("Porsche", "Porsche"),
    ("RAM", "RAM"),
    ("Rivian", "Rivian"),
    ("Rolls-Royce", "Rolls-Royce"),
    ("Subaru", "Subaru"),
    ("Tesla", "Tesla"),
    ("Toyota", "Toyota"),
    ("Volkswagen", "Volkswagen"),
    ("Volvo", "Volvo"),
]

class PredictionForm(forms.Form):
    brand = forms.ChoiceField(choices=BRAND_CHOICES, label="Car Brand")
    model = forms.CharField(label="Car Model")
    year = forms.IntegerField(label="Year")
    transmission = forms.ChoiceField(choices=[("Manual", "Manual"), ("Automatic", "Automatic"), ("Other", "Other")], label="Transmission")
    fuel_type = forms.ChoiceField(choices=[("E85 Flex Fuel", "E85 Flex Fuel"), ("Gasoline", "Gasoline"), ("Hybrid", "Hybrid"),
                                            ("Diesel", "Diesel"), ("Plug-In Hybrid", "Plug-In Hybrid"), ("not supported", "not supported")], 
                                   label="Fuel Type")
    mileage = forms.IntegerField(label="Mileage")
    clean_title = forms.ChoiceField(choices=[("Yes", "Yes"), ("No", "No")], label="Clean Title")
    accident_history = forms.ChoiceField(choices=[("Yes", "Yes"), ("No", "No")], label="Accident History")
    engine_size = forms.FloatField(label="Engine Size (in liters)")
    horsepower = forms.IntegerField(label="Horsepower")
