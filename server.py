from flask import Flask, request

app = Flask(__name__)

# Endpoint to receive CF values from webview instances
@app.route('/send_cf', methods=['POST'])
def send_cf():
    data = request.json
    if 'cf' in data:
        cf_value = data['cf']
        # Process cf_value here 
		##your code below
        print(f"Received CF value: {cf_value}")  # You can add your processing logic here
        return {"message": "CF value received and processing started"}, 200
    else:
        return {"message": "CF value missing"}, 400

# Start the Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
