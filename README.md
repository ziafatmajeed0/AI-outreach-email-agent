# 🤖 AI Outreach Email Agent

This project is a fully automated email outreach system that sends personalized business proposals to a list of contacts — **on your schedule, automatically, and at scale**.

It uses Python + GitHub Actions to send emails **daily, without manual effort**, even while you sleep.

---

## 🚀 Features

- ✅ Sends personalized proposals to **thousands of contacts**
- ✅ Reads leads from an Excel file (`emails.xlsx`)
- ✅ Sends emails using **Gmail SMTP**
- ✅ Automatically runs on a custom schedule (via GitHub Actions)
- ✅ Skips duplicate sends with date tracking (`last_sent.txt`)
- ✅ 100% Free (No server or cloud costs)

---

## 🧠 Tech Stack

- **Python** – Logic, proposal generation, email sending
- **pandas + openpyxl** – For Excel handling
- **GitHub Actions** – To run the script on schedule in the cloud
- **Gmail SMTP** – For secure email delivery

---

## 📁 File Structure
.
- ├── emails.xlsx # Your list of contacts
- ├── email_sender.py # Main script to send emails
- ├── last_sent.txt # File to track if emails were already sent today
- └── .github/
- └── workflows/
- └── send_email.yml # GitHub Actions workflow

