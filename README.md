# Real-Time-Fire_forest_Detection

## 📌 Project Overview
A real-time forest fire detection system using NASA VIIRS satellite data and Machine Learning. The system fetches live satellite data, predicts fire severity using a Random Forest model (99.54% accuracy), and sends automatic email/SMS alerts when high fire is detected.

---

## 🎯 Problem Statement
Forest fires cause massive environmental and economic damage every year. Early detection can significantly reduce this damage. Traditional manual monitoring is slow and inefficient. This AI-powered system provides real-time automatic fire detection using satellite data.

---

## 🛰️ Data Source
- **Source:** NASA FIRMS (Fire Information for Resource Management System)
- **Satellite:** VIIRS (Visible Infrared Imaging Radiometer Suite)
- **Data Points:** 5,52,312 records
- **Features:** Latitude, Longitude, Brightness Temperature (TI4/TI5), FRP (Fire Radiative Power), Scan, Track, Acquisition Time, Confidence, Day/Night

---

## 🤖 Model Details

| Parameter | Value |
|-----------|-------|
| Algorithm | Random Forest Classifier |
| Training Data | 5.5 Lakh records |
| Test Data | 1.1 Lakh records |
| Accuracy | 99.54% |
| Precision | 99% |
| Recall | 100% |
| F1-Score | 99% |

### Features Used:
- Latitude, Longitude
- Brightness TI4, Brightness TI5
- Temperature Difference (TI4 - TI5)
- Temperature Ratio (TI4 / TI5)
- Fire Risk Score
- FRP per Area
- Scan, Track, Acquisition Time
- Confidence, Day/Night

---

## 📁 Project Structure
AI Forest Fire Prediction/
│
├── app.py # Streamlit web application
├── satellite.py # NASA API integration
├── predict.py # Model prediction logic
├── alert.py # Email & SMS alerts
├── config.py # API keys configuration
├── test.py # Testing script
│
├── fire_model.pkl # Trained Random Forest model
├── scaler.pkl # Feature scaler
├── feature_columns.pkl # Feature names
├── fire_dataset.csv # Training dataset (5.5L records)
│
└── requirements.txt # Python dependencies




---

## 💻 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Pandas, NumPy | Data processing |
| Scikit-learn | Machine Learning (Random Forest) |
| Streamlit | Web application framework |
| Plotly | Interactive maps & visualizations |
| NASA FIRMS API | Real-time satellite data |
| SMTP | Email alerts |
| TextBelt API | SMS alerts |

---

## 🔄 System Workflow

---

## 📊 How Prediction Works

### Input Parameters:

| Parameter | Description | Range |
|-----------|-------------|-------|
| Latitude | Geographic coordinate | -90 to 90 |
| Longitude | Geographic coordinate | -180 to 180 |
| Brightness TI4 | Channel I4 temperature (K) | 300-370K |
| Brightness TI5 | Channel I5 temperature (K) | 290-310K |
| FRP | Fire Radiative Power | 0-1500+ |
| Scan | Satellite scan angle | 0.3-0.8 |
| Track | Satellite track angle | 0.3-0.8 |

### Output:

| Severity | Icon | Action |
|----------|------|--------|
| No Fire | 🟢 | Safe - No action needed |
| Low Fire | 🟡 | Monitor situation |
| High Fire | 🔴 | Emergency - Alert authorities |

---

## 🚀 How to Run

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt



Step 2: Configure API Keys

NASA_API_KEY = "your_nasa_api_key"
EMAIL_FROM = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
PHONE_NUMBER = "+91XXXXXXXXXX"
EMAIL_TO = "alert@example.com"



Step 3: Run the Application
streamlit run app.py



Step 4: Test the System
Open browser at http://localhost:8501
Go to Manual Prediction tab
Enter parameters:
FRP = 0 → No Fire
FRP = 3 → Low Fire
FRP = 10 → High Fire

Click Analyze Fire Risk

📧 Alert System
When high fire is detected:
Email Alert: Sent to configured email address
SMS Alert: Sent to configured phone number (1 free SMS/day via TextBelt)

🗺️ Live Satellite Feed
Fetches real-time data from NASA FIRMS API
Displays fire locations on interactive map
Shows fire intensity with color coding
Updates every 3 hours (satellite overpass frequency)



Classification Report:
              precision    recall  f1-score   support
     No Fire       1.00      0.75      0.86         4
    Low Fire       0.99      1.00      1.00     73212
   High Fire       1.00      0.99      0.99     37247

    accuracy                           1.00    110463




🔮 Future Scope
Add weather data (wind speed, humidity, temperature)

Mobile app integration
Deploy on cloud (AWS/GCP/Azure)
WhatsApp alerts integration
Historical fire trend analysis
Fire risk prediction for next 24 hours

👨‍💻 Author
Project: Satellite Forest Fire Detection System
Technology: Python, Streamlit, Machine Learning, NASA API
Accuracy: 99.54%

📝 Conclusion
This system successfully demonstrates the use of satellite data and machine learning for real-time forest fire detection. With 99.54% accuracy and automatic alert capabilities, it provides a reliable solution for early fire warning and prevention.

