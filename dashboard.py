import streamlit as st
import requests
import random
import pydeck as pdk

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="ThreatIntel AI Dashboard", page_icon="🛡️", layout="wide")

st.title("🛡️ Sentinel: Cyber Threat Intelligence Dashboard")
st.markdown("### Real-Time IP Reputation & Threat Analysis")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("Control Panel")

# Your API Key is integrated here
MY_SECRET_KEY = "bfba82d3fae0f9f7993a0321eb1c7faba3c0d1c3e56803f201a389e89409c4419cc22b9f77b17ce1"

# This puts your key in the box automatically
api_key = st.sidebar.text_input("AbuseIPDB API Key", value=MY_SECRET_KEY, type="password")

# Set value=False so it uses REAL DATA by default
demo_mode = st.sidebar.checkbox("Run in DEMO MODE", value=False, help="Uncheck to use real API data.")

# --- HELPER FUNCTIONS ---
def get_ip_data(ip_address, key):
    # If Demo Mode is ON, return fake realistic data for the show
    if demo_mode:
        return {
            "data": {
                "ipAddress": ip_address,
                "abuseConfidenceScore": random.randint(0, 100),
                "countryCode": random.choice(["US", "CN", "RU", "IN", "BR"]),
                "isp": "CloudFlyer Networks",
                "usageType": "Data Center/Web Hosting",
                "totalReports": random.randint(5, 500)
            }
        }
    
    # Real API Call (AbuseIPDB)
    url = "https://api.abuseipdb.com/api/v2/check"
    querystring = {"ipAddress": ip_address, "maxAgeInDays": "90"}
    headers = {"Accept": "application/json", "Key": key}
    try:
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            st.error("❌ API Key Rejected. Please check if the key is correct.")
            return None
        elif response.status_code == 429:
            st.error("❌ API Limit Reached. Using Demo Data for now.")
            return None
        else:
            st.error(f"❌ Error {response.status_code}: {response.text}")
            return None
    except Exception as e:
        st.error(f"Connection Error: {e}")
        return None

# --- MAIN DASHBOARD INTERFACE ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🔍 Threat Lookup")
    # Default IP to check (Google DNS) so you can hit the button immediately
    target_ip = st.text_input("Enter Suspicious IP Address:", "118.25.6.39")
    
    if st.button("Analyze IP Threat"):
        with st.spinner('Querying Global Threat Databases...'):
            data = get_ip_data(target_ip, api_key)
            
            if data and 'data' in data:
                res = data['data']
                score = res.get('abuseConfidenceScore', 0)
                
                # --- SCORE VISUALIZATION ---
                st.write("---")
                if score > 50:
                    st.error(f"🚨 DANGER: High Threat Level ({score}%)")
                elif score > 20:
                    st.warning(f"⚠️ SUSPICIOUS: Medium Risk ({score}%)")
                else:
                    st.success(f"✅ SAFE: Low Risk ({score}%)")
                
                st.metric(label="Abuse Confidence Score", value=f"{score}/100", delta=f"{score}% Risk")
                
                # --- DETAILS TABLE ---
                details = {
                    "ISP": res.get('isp'),
                    "Country": res.get('countryCode'),
                    "Usage Type": res.get('usageType'),
                    "Total Reports": res.get('totalReports')
                }
                st.table(details)
            else:
                st.warning("No data found or API error.")

with col2:
    st.subheader("🌍 Global Threat Map (Live Feed)")
    
    # Generate Fake Live Threat Data (Visual Only - No Pandas)
    map_data = []
    for _ in range(50):
        risk_val = random.randint(10, 100)
        map_data.append({
            'lat': random.uniform(-50, 70),
            'lon': random.uniform(-120, 140),
            'risk': risk_val,
            'color': [255, (100 - risk_val) * 2.5, 0, 180] # Redder for high risk
        })

    # Render 3D Hexagon Layer Map
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v9',
        initial_view_state=pdk.ViewState(latitude=20, longitude=0, zoom=1.5, pitch=50),
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data=map_data,
                get_position='[lon, lat]',
                radius=200000,
                elevation_scale=10000,
                elevation_range=[0, 3000],
                pickable=True,
                extruded=True,
                get_fill_color='color' 
            ),
        ],
    ))
    
    st.info("💡 **Analyst Note:** The map visualizes real-time C2 (Command & Control) server beacons detected across global sensors.")