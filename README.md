# intervue_login.py
# Intervue.io - Login Automation

This project automates the login flow on [Intervue.io](https://www.intervue.io) for **Company Login** using Selenium and Python.

If login fails, a screenshot is captured automatically inside the `screenshots/` folder.

---

## 🔥 Flow Automated

1. Open [https://www.intervue.io](https://www.intervue.io)
2. Click **Login** (top-right corner)
3. Click **Company Login** (Green button)
4. Click **Login with Email**
5. Enter provided credentials
6. Submit and validate successful login
7. If login fails, capture a screenshot with timestamp.

---

## 🛠 Tech Stack

- Python 3.7+
- Selenium 4.x
- WebDriver-Manager (auto-downloads ChromeDriver)

---

## 🏗 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/intervue-login-automation.git
   cd intervue-login-automation
