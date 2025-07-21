# call_handler.py
import csv
import requests
import os

def call_candidate(name, number, date, time):
    # Get Agent ID and API Key from environment variables
    agent_id = os.environ.get("ELEVENLABS_AGENT_ID")
    api_key = os.environ.get("ELEVENLABS_API_KEY")

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

def start_calls_from_csv():
    with open("candidates.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Status'] == 'Pending':
                call_candidate(
                    row['Candidate_Name'],
                    row['Phone_Number'],
                    row['Date'],
                    row['Time']
                )
