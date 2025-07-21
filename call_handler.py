import csv
import requests
import os

def call_candidate(name, number, date, time):
    agent_id = os.environ.get("ELEVENLABS_AGENT_ID")
    api_key = os.environ.get("ELEVENLABS_API_KEY")

    if not agent_id or not api_key:
        print("❌ ELEVENLABS_AGENT_ID or ELEVENLABS_API_KEY is missing in environment variables.")
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

def start_calls_from_csv():
    with open("candidates.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Status'].lower() == 'pending':
                call_candidate(
                    row['Candidate_Name'],
                    row['Phone_Number'],
                    row['Date'],
                    row['Time']
                )
