import requests

def call_candidate(name, number, date, time):
    agent_id = "agent_01k0dz6eqjf5xbnt9p5aztm02x"
    url = f"https://api.elevenlabs.io/v1/agents/{agent_id}/calls"  # ✅ FIXED endpoint

    payload = {
        "phone_number": number,
        "dynamic_variables": {
            "Candidate_Name": name,
            "Date": date,
            "Time": time
        }
    }

    headers = {
        "xi-api-key": "sk_f7db91804aafc36f5e4c5498c82eadf8d35724fc394bf510",  # ✅ Your key
        "Content-Type": "application/json"
    }

    r = requests.post(url, json=payload, headers=headers)
    print("✅ Call sent to:", name, number)
    print("Response:", r.status_code, r.text)
