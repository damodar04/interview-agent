# call_handler.py
import csv
import requests
import os # Import the os module

def call_candidate(name, number, date, time):
    # Get Agent ID and API Key from environment variables
    agent_id = os.environ.get("agent_01k0dz6eqjf5xbnt9p5aztm02x")
    api_key = os.environ.get("sk_731ae5efda6af78f64cd48354d3e4d95de9824f23c723f45")

    if not agent_id or not api_key:
        print("Error: ELEVENLABS_AGENT_ID and ELEVENLABS_API_KEY must be set as environment variables.")
        return

    url = f"https://api.elevenlabs.io/v1/agents/{agent_id}/calls"

    payload = {
        "phone_number": number,
        "dynamic_variables": {
            "Candidate_Name": name,
            "Date": date,
            "Time": time
        }
    }

    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    r = requests.post(url, json=payload, headers=headers)
    print("✅ Call sent to:", name, number)
    print("Response:", r.status_code, r.text)

# ... (rest of the file remains the same)
