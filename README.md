---
title: "🔥 Heat Flux ML Regression"
emoji: 🔬
colorFrom: red
colorTo: yellow
sdk: streamlit
app_file: app.py
pinned: false
license: mit
tags:
  - regression
  - streamlit
  - machine-learning
  - heat-flux
  - engineering
---


# 🔥 Heat Flux ML Regression – CHF Tahmin Uygulaması

Bu proje, deneysel mühendislik verilerini kullanarak **kritik ısı akısını (CHF)** tahmin eden bir makine öğrenmesi modelini içermektedir. Uygulama **Streamlit** ile oluşturulmuş ve kullanıcı dostu bir arayüz sunmaktadır.

## 📦 Kullanılan Veri Seti
- Kaggle Playground Series S3E15  
- [Veri Seti Bağlantısı](https://www.kaggle.com/competitions/playground-series-s3e15/data)

## 🎯 Hedef
Verilen deneysel koşullar (basınç, kütle akısı, boru geometrisi vb.) altında oluşan `chf_exp [MW/m2]` değerini tahmin etmek.

## 🧠 Kullanılan Model
- Random Forest Regressor
- RMSE: ~1.73, R²: ~0.27

## ⚙️ Gerekli Dosyalar
- `rf_model.pkl`: Eğitilmiş model
- `model_columns.pkl`: One-hot encoded sütun listesi
- `app.py`: Streamlit arayüzü

Uygulama Ekranı
Kullanıcıdan deneysel koşullar alınır ve tahmini CHF değeri hesaplanır.

Geliştirilebilir Noktalar
LightGBM, XGBoost gibi daha güçlü modeller denenebilir.

Hyperparameter tuning yapılabilir.

Feature engineering (etkileşimli sütunlar) geliştirilebilir.
⚠️ Bu proje eğitim amaçlıdır.

## 🚀 Uygulamayı Çalıştırmak
```bash
pip install -r requirements.txt
streamlit run app.py

