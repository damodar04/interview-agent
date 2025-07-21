from flask import Flask, request, jsonify
from call_handler import start_calls_from_csv
from response_handler import handle_response

app = Flask(__name__)

@app.route("/")
def index():
    return "✅ Interview Agent Running"

@app.route("/start-calls")
def start_calls():
    start_calls_from_csv()
    return "✅ Calls started"

@app.route("/log-response", methods=["POST"])
def log_response():
    return handle_response(request.json)

# ✅ This is the key fix
@app.route("/tools", methods=["GET"])
def list_tools():
    return jsonify({
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
    })
