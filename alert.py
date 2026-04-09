import requests
import smtplib
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from config import EMAIL_FROM, EMAIL_PASSWORD, EMAIL_TO, PHONE_NUMBER

def send_sms(lat, lon, confidence):
    """Send SMS alert"""
    url = "https://textbelt.com/text"
    message = f"FIRE ALERT! High fire at {lat}, {lon}. Confidence: {confidence:.1f}%"
    
    payload = {
        "phone": PHONE_NUMBER,
        "message": message,
        "key": "textbelt"
    }
    
    try:
        response = requests.post(url, data=payload)
        return response.json().get('success', False)
    except:
        return False

def send_email(lat, lon, confidence):
    """Send Email alert"""
    msg = MIMEMultipart()
    msg['Subject'] = 'FIRE ALERT'
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    
    body = f"""
    HIGH FIRE ALERT!
    Location: {lat}, {lon}
    Confidence: {confidence:.1f}%
    Time: {datetime.now()}
    Take immediate action!
    """
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False

def send_alerts(lat, lon, confidence):
    """Send both alerts"""
    email_status = send_email(lat, lon, confidence)
    sms_status = send_sms(lat, lon, confidence)
    return email_status, sms_status