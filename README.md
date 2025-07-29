
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

```
.
├── emails.xlsx          # Your list of contacts
├── email_sender.py      # Main script to send emails
├── last_sent.txt        # File to track if emails were already sent today
└── .github/
    └── workflows/
        └── send_email.yml  # GitHub Actions workflow
```

---

## ✉️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-outreach-agent.git
cd ai-outreach-agent
```

### 2. Add your email list

Create `emails.xlsx` with the following columns:

| email              | name  | business        |
|-------------------|-------|-----------------|
| client1@gmail.com | Ali   | Ali Garments    |
| client2@gmail.com | Sara  | Sara Jewelry    |

### 3. Set up Gmail SMTP

- Enable 2-Step Verification on your Gmail account
- Generate an **App Password** for "Mail"
- Go to your GitHub Repo → **Settings > Secrets and variables > Actions**
- Add the following secrets:
  - `GMAIL_USER` = your Gmail address (e.g., `yourname@gmail.com`)
  - `GMAIL_PASS` = your App Password

### 4. Customize schedule (Optional)

In `.github/workflows/send_email.yml`, you can modify the `cron:` schedule to match your desired send times.  
Currently, it's set to run at **5:15 AM and 5:30 AM PKT** on **Mon, Wed, Fri, Sun**.

```yaml
schedule:
  - cron: '15 0 * * 1,3,5,0'
  - cron: '30 0 * * 1,3,5,0'
```

> 🕐 These are in UTC. PKT = UTC+5

---

## 🛡️ Safeguards

- Uses `last_sent.txt` to **prevent duplicate sends** in a single day (even if GitHub runs the job multiple times)

---

## 💬 Example Output

```bash
Started at: 2025-07-29 00:15:01
Sent to client1@gmail.com
Sent to client2@gmail.com
Emails sent and marked as sent for today.
```

---

## 📌 Use Cases

- Freelancers & agencies doing cold outreach
- E-commerce or SaaS lead generation
- Automated onboarding offers or updates
- Sending updates to newsletter lists

---

## 📞 Need Help?

Message me on [LinkedIn](https://linkedin.com/in/ziafatmajeed) or open an issue here.  
Happy to help you automate your outreach, too!

---

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

**Built by [Ziafat Majeed](https://linkedin.com/in/ziafatmajeed) **
