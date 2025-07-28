import pandas as pd
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import os

EMAIL_ADDRESS = os.environ["GMAIL_USER"]
EMAIL_PASSWORD = os.environ["GMAIL_PASS"]

def generate_proposal(name, business):
    return f"""\
Hi {name},

I hope you're doing well. I'm reaching out from Boostify Ecom — we help businesses like {business} grow using AI automation and Shopify expertise.

We offer:
- Shopify Store Setup & Management
- Facebook & Google Ads
- AI-based Sales Automation

Let us know if you'd like to scale your business effortlessly.

Regards,  
Ziafat Majeed  
Boostify Ecom  
"""

def send_email(to_email, subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print(f"Sent to {to_email}")

# Prevent double sending
today = datetime.utcnow().date()
stamp_file = "last_sent.txt"

if os.path.exists(stamp_file):
    with open(stamp_file, "r") as f:
        if f.read().strip() == str(today):
            print("Already sent today.")
            exit()

# Load recipients
df = pd.read_excel("emails.xlsx")
for _, row in df.iterrows():
    body = generate_proposal(row["name"], row["business"])
    send_email(row["email"], "Let's grow your business with AI", body)

# Mark as sent
with open(stamp_file, "w") as f:
    f.write(str(today))
