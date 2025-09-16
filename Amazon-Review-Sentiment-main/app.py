from flask import Flask, render_template, request
from utils.inference import predict_text
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form.get("review_text", "")
    try:
        prediction = predict_text(text)
        return render_template("result.html", text=text, prediction=prediction)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"Prediction failed: {e}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
