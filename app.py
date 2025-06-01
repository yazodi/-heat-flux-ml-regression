import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 🎯 Başlık
st.title("💥 CHF (Kritik Isı Akısı) Tahmini")
st.write("Bu uygulama, deneysel koşullara göre kritik ısı akısını (chf_exp) tahmin eder.")

# 🎯 Giriş Değerleri
author = st.selectbox("Yazar", ["Thompson", "Beus", "Other"])
geometry = st.selectbox("Geometri", ["tube", "annulus", "Other"])
pressure = st.number_input("Basınç [MPa]", min_value=0.0, max_value=30.0, value=10.0)
mass_flux = st.number_input("Kütle Akısı [kg/m2-s]", min_value=0.0, max_value=10000.0, value=2000.0)
x_e_out = st.number_input("Çıkış Buhar Kalitesi (x_e_out)", value=0.1)
D_e = st.number_input("Dış Çap [mm] (D_e)", value=10.0)
D_h = st.number_input("Hidrolik Çap [mm] (D_h)", value=10.0)
length = st.number_input("Boru Uzunluğu [mm]", value=1000.0)

# 🎯 Veriyi DataFrame'e çevir
input_data = pd.DataFrame({
    "author": [author],
    "geometry": [geometry],
    "pressure [MPa]": [pressure],
    "mass_flux [kg/m2-s]": [mass_flux],
    "x_e_out [-]": [x_e_out],
    "D_e [mm]": [D_e],
    "D_h [mm]": [D_h],
    "length [mm]": [length]
})

# ⚙️ One-hot encode
input_data = pd.get_dummies(input_data)

# Eğitim setinde olup testte olmayan sütunları ekle
model_columns = joblib.load("model_columns.pkl")  # Kaydetmemiz gerekiyor
for col in model_columns:
    if col not in input_data.columns:
        input_data[col] = 0

input_data = input_data[model_columns]

# 🎯 Modeli yükle
model = joblib.load("rf_model.pkl")

# 🧠 Tahmin et
if st.button("Tahmin Et"):
    prediction = model.predict(input_data)[0]
    st.success(f"Tahmin Edilen CHF Değeri: {prediction:.2f} MW/m2")
