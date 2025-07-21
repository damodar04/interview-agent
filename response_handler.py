import csv

def handle_response(data):
    name = data.get("Candidate_Name") or data.get("candidate_name") or "Unknown"
    status = data.get("Status") or data.get("status") or "Unknown"
    new_date = data.get("New_Date") or data.get("new_date")
    new_time = data.get("New_Time") or data.get("new_time")

    updated_rows = []
    with open("candidates.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Candidate_Name"] == name:
                row["Status"] = status
                if status.lower() == "reschedule" and new_date and new_time:
                    row["Date"] = new_date
                    row["Time"] = new_time
            updated_rows.append(row)

    with open("candidates.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=updated_rows[0].keys())
        writer.writeheader()
        writer.writerows(updated_rows)

    return {"message": "✅ Response saved"}
