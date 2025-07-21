import requests

def call_candidate(name, number, date, time):
    agent_id = "agent_01k0dz6eqjf5xbnt9p5aztm02x"
    url = f"https://api.elevenlabs.io/v1/agents/{agent_id}/call"

    payload = {
        "phone_number": number,
        "dynamic_variables": {
            "Candidate_Name": name,
            "Date": date,
            "Time": time
        }
    }

    headers = {
        "xi-api-key": "sk_21ac555177b458ab8bcb7c3409c0d85663bcc3afa860e8c0",
        "Content-Type": "application/json"
    }

    r = requests.post(url, json=payload, headers=headers)
    print("✅ Call sent to:", name, number)
    print("Response:", r.text)