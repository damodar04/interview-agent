# app.py
from flask import Flask, request, jsonify
from call_handler import start_calls_from_csv
from response_handler import handle_response

app = Flask(__name__)

@app.route('/start-calls', methods=['GET'])
def start_calls():
    start_calls_from_csv()
    return jsonify({"message": "✅ Calls initiated"})

@app.route('/log-response', methods=['POST'])
def log_response():
    return handle_response(request.json)
@app.route("/tools", methods=["GET"])
def list_tools():
    return {
        "tools": [
            {
                "name": "log_response",
                "description": "Log candidate's interview response",
                "type": "action",
                "parameters": {
                    "Candidate_Name": "string",
                    "Status": "string",
                    "New_Date": "string",
                    "New_Time": "string"
                }
            }
        ]
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
