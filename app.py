from flask import Flask, request, jsonify
from call_handler import call_candidate
from response_handler import handle_response

app = Flask(__name__)

@app.route('/start-calls')
def start_calls():
    import csv
    with open("candidates.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Status'] == 'Pending':
                call_candidate(row['Candidate_Name'], row['Phone_Number'], row['Date'], row['Time'])
    return "✅ Calls triggered"

@app.route('/log-response', methods=['POST'])
def log_response():
    return handle_response(request.json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)