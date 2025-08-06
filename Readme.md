# 💬 M0tB0t — Your WhatsApp Hype Buddy

**M0tB0t** is a simple Python bot that sends you motivational images twice a day straight to your WhatsApp — because sometimes we all need a little kick to keep going. It grabs content from [r/GetMotivated](https://www.reddit.com/r/GetMotivated) and sends it to you using Twilio.

No fluff, just motivation — morning and Night

---

## ✨ What It Does

- 🖼️ Sends inspirational image posts from Reddit
- ⏰ Runs twice a day (default: 9 AM and 11 PM)
- 📲 Delivers messages directly to your WhatsApp via Twilio
- 🧠 Built in Python with love and caffeine

---

## 🛠️ Setup Guide

### 1. Clone this repo
```bash
git clone https://github.com/your-username/M0tB0t.git
cd M0tB0t
```
### 2.Install the required packages

```bash
pip install -r requirements.txt
```
### 3. Set up your .env file

Create a .env file in the project folder and add:
`
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=+1415xxxxxxx
MY_PHONE_NUMBER=+91xxxxxxxxxx
`

### 4.Running the Bot

`python3 motbot.py`

### 📂 Project Structure
```bash
M0tB0t/
├── motbot.py           
├── .env               
├── .gitignore          
├── requirements.txt    
└── README.md          
```
