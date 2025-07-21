from flask import Flask, request
from call_handler import start_calls_from_csv
from response_handler import handle_response
from call_handler import call_candidate

app = Flask(__name__)

@app.route('/start-calls')
def start_calls():
    start_calls_from_csv()
    return '✅ All calls triggered'

@app.route('/log-response', methods=['POST'])
def log_response():
    return handle_response(request.json)

# ✅ NEW: Accept direct /calls POST requests from ElevenLabs or Postman
@app.route('/calls', methods=['POST'])
def direct_call():
    data = request.get_json()
    name = data["dynamic_variables"].get("Candidate_Name", "Candidate")
    number = data["phone_number"]
    date = data["dynamic_variables"].get("Date", "")
    time = data["dynamic_variables"].get("Time", "")

    call_candidate(name, number, date, time)

    return {"message": "📞 Call triggered via /calls"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
