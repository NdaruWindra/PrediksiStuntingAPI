import pickle
import os

# Mendapatkan path absolut dari direktori saat ini (direktori tempat model.py berada)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Path ke file model
model_file = os.path.join(base_dir, "stunting_model.sav")

# Load model from pickle file
with open(model_file, "rb") as f:
    stunting_model_knn = pickle.load(f)

# Function to predict stunting
def predict_stunting(umur, jenis_kelamin, tinggi_badan):
    # Validasi umur
    if umur < 0 or umur > 60:
        return {'error': 'Umur harus antara 0 dan 60 bulan.'}

    # Lakukan prediksi menggunakan model KNN
    input_data = [[umur, jenis_kelamin, tinggi_badan]]
    stun_prediction = stunting_model_knn.predict(input_data)

    if stun_prediction[0] == 2:
        stun_diagnosis = 'Perkembangan Normal'
    elif stun_prediction[0] == 3:
        stun_diagnosis = 'Perkembangan Tinggi'
    elif stun_prediction[0] == 1:
        stun_diagnosis = 'Perkembangan Stunting'
    elif stun_prediction[0] == 0:
        stun_diagnosis = 'Perkembangan Sangat Stunting'
    else:
        stun_diagnosis = 'Diagnosis tidak dikenal'

    return {'stun_diagnosis': stun_diagnosis}
