import csv

def handle_response(data):
    name = data["Candidate_Name"]
    status = data["Status"]
    new_date = data.get("New_Date")
    new_time = data.get("New_Time")

    updated_rows = []
    with open("candidates.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Candidate_Name"] == name:
                row["Status"] = status
                if status == "Reschedule":
                    row["Date"] = new_date
                    row["Time"] = new_time
            updated_rows.append(row)

    with open("candidates.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=updated_rows[0].keys())
        writer.writeheader()
        writer.writerows(updated_rows)

    return {"message": "✅ Response saved"}