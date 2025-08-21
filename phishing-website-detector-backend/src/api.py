from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)



try:
    print("Loading webcode vectorizer...")
    webcode_vectorizer = joblib.load("/workspaces/phishing-website-detector-backend/utilities/vectorizer_webcode.joblib")
    print("Loading webcode model...")
    webcode_model = joblib.load("/workspaces/phishing-website-detector-backend/utilities/xgboost_webcode.joblib")
    print("Loading URL vectorizer...")
    url_vectorizer = joblib.load("/workspaces/phishing-website-detector-backend/utilities/vectorizer_url.joblib")
    print("Loading URL model...")
    url_model = joblib.load("/workspaces/phishing-website-detector-backend/utilities/linearsvc_url.joblib")
    print("All models loaded successfully!")
except Exception as e:
    print(f"Error loading models: {e}")
    raise e


@app.route('/predict/webcode', methods=['POST'])
def predict_webcode():
    data = request.json
    text = data['text']
    vec = webcode_vectorizer.transform([text])
    pred = int(webcode_model.predict(vec)[0])
    return jsonify({"prediction": pred})

@app.route('/predict/url', methods=['POST'])
def predict_url():
    data = request.json
    text = data['text']
    vec = url_vectorizer.transform([text])
    pred = int(url_model.predict(vec)[0])
    return jsonify({"prediction": pred})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)