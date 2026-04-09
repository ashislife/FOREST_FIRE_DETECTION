import pandas as pd
import joblib

# Load model once
model = joblib.load('fire_model.pkl')
scaler = joblib.load('scaler.pkl')
features = joblib.load('feature_columns.pkl')

def predict_fire(lat, lon, ti4, ti5, scan, track, acq_time, frp=1):
    """Predict fire severity"""
    
    # Feature engineering
    temp_diff = ti4 - ti5
    temp_ratio = ti4 / (ti5 + 0.01)
    fire_risk = (ti4 - 300) * 0.4 + temp_diff * 0.3
    frp_area = frp / (scan * track + 0.01)
    
    # Create input
    data = [[lat, lon, ti4, ti5, scan, track, acq_time, 1, 1, 
             temp_diff, temp_ratio, fire_risk, frp_area]]
    
    input_df = pd.DataFrame(data, columns=features)
    input_scaled = scaler.transform(input_df)
    
    pred = model.predict(input_scaled)[0]
    prob = max(model.predict_proba(input_scaled)[0])
    
    return pred, prob

def get_severity_text(pred):
    if pred == 0:
        return "No Fire", "🟢"
    elif pred == 1:
        return "Low Fire", "🟡"
    else:
        return "High Fire", "🔴"