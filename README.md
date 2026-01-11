# 🛡️ Sentinel: Real-Time Cyber Threat Intelligence Dashboard

**Sentinel** is a lightweight, Python-based Cyber Threat Intelligence (CTI) dashboard designed for Security Operations Centers (SOCs). It integrates real-time threat feeds to automate IP reputation analysis, allowing security analysts to instantly verify suspicious IP addresses and visualize global threat vectors.

---

## 🚀 Features
* **Real-Time IP Reputation:** Fetches live "Abuse Confidence Scores" from the AbuseIPDB API.
* **Risk Scoring:** Automatically categorizes IPs as **Safe**, **Suspicious**, or **High Risk**.
* **ISP & Geo-Location:** Displays Internet Service Provider (ISP) data, usage type (Data Center/Residential), and Country.
* **3D Global Threat Map:** Visualizes simulated threat beacons on a 3D interactive globe.
* **Analyst Mode:** Includes a "Demo Mode" for offline presentation and testing.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Framework:** Streamlit (for UI/Dashboard)
* **API:** AbuseIPDB (Threat Intelligence Feed)
* **Visualization:** PyDeck (3D Geospatial Mapping)
* **Network:** Requests library

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/sentinel-dashboard.git](https://github.com/your-username/sentinel-dashboard.git)
cd sentinel-dashboard
2. Install Dependencies
You can install the required libraries using pip:

Bash

pip install streamlit requests pydeck
🔑 Configuration (API Key)
To use the Real-Time Analysis feature, you need a free API Key from AbuseIPDB.

Sign up and generate an API Key.

Open dashboard.py.

Paste your key into the MY_SECRET_KEY variable:

Python

MY_SECRET_KEY = "YOUR_API_KEY_HERE"
Alternatively, you can enter the key manually in the dashboard sidebar at runtime.

▶️ Usage
Run the dashboard using Streamlit:

Bash

streamlit run dashboard.py
The application will automatically open in your default web browser at http://localhost:8501.

How to Use:

Enter IP: Type a suspicious IP address (e.g., 118.25.6.39) in the "Threat Lookup" box.

Analyze: Click the Analyze IP Threat button.

View Results: Check the Risk Score, ISP details, and visual indicators.

📂 Project Structure
📁 sentinel-dashboard/
├── dashboard.py       # Main application source code
├── README.md          # Project documentation
└── requirements.txt   # List of dependencies
⚠️ Disclaimer
This tool is intended for educational and defensive purposes only. It is designed to help security analysts identify threats. The "Global Threat Map" visualizes simulated data for demonstration purposes.

👤 Author
Hirday Shevkani

Role: Cybersecurity Intern @ Elevate Labs

Date: January 2026
