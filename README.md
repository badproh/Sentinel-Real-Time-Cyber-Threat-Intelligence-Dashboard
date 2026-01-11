# 🛡️ Sentinel: Real-Time Cyber Threat Intelligence Dashboard

**Sentinel** is a lightweight, Python-based Cyber Threat Intelligence (CTI) dashboard designed for Security Operations Centers (SOCs). It integrates real-time threat feeds to automate IP reputation analysis, allowing security analysts to instantly verify suspicious IP addresses and visualize global threat vectors.

---

## 🚀 Features
* **Real-Time IP Reputation:** Fetches live "Abuse Confidence Scores" from the AbuseIPDB API.
* **Risk Scoring:** Automatically categorizes IPs as **Safe**, **Suspicious**, or **High Risk**.
* **ISP & Geo-Location:** Displays Internet Service Provider (ISP) data, usage type (Data Center/Residential), and Country.
* **3D Global Threat Map:** Visualizes simulated threat beacons on a 3D interactive globe using PyDeck.
* **Analyst Mode:** Includes a "Demo Mode" fallback for offline presentation and testing.

---

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Framework:** [Streamlit](https://streamlit.io/) (UI/Dashboard)
* **API:** [AbuseIPDB](https://www.abuseipdb.com/) (Threat Intelligence Feed)
* **Visualization:** PyDeck (3D Geospatial Mapping)
* **Networking:** Requests library

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR-USERNAME/sentinel-dashboard.git](https://github.com/YOUR-USERNAME/sentinel-dashboard.git)
cd sentinel-dashboard
2. Install Dependencies
Bash

pip install -r requirements.txt
3. API Configuration
To use the Real-Time Analysis feature, you need a free API Key from AbuseIPDB.

Open dashboard.py.

Find the variable MY_SECRET_KEY (around line 14).

Paste your API key inside the quotes:

Python

MY_SECRET_KEY = "YOUR_ACTUAL_API_KEY_HERE"
(Note: The code is pre-configured to handle API errors gracefully).

▶️ Usage
Run the dashboard locally using Streamlit:

Bash

streamlit run dashboard.py
The application will automatically open in your default web browser at http://localhost:8501.

How to Use:

Enter IP: Type a suspicious IP address (e.g., 118.25.6.39 or 8.8.8.8) in the "Threat Lookup" box.

Analyze: Click the Analyze IP Threat button.

View Results: Check the Risk Score, ISP details, and visual indicators.

Visualize: Observe the "Global Threat Map" on the right panel for simulated C2 beacon activity.

📂 Project Structure
Plaintext

📁 sentinel-dashboard/
├── dashboard.py       # Main application source code
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
└── .gitignore         # Files to ignore (e.g., local configs)
⚠️ Disclaimer
This tool is intended for educational and defensive purposes only. It is designed to help security analysts identify threats. The "Global Threat Map" visualizes simulated data for demonstration purposes to represent CTI capabilities.

👤 Author
Hirday Shevkani

Role: Cybersecurity Intern @ Elevate Labs

Date: January 2026
