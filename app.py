from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PLACE_ID = os.getenv("GOOGLE_PLACE_ID")

@app.route("/reviews")
def get_reviews():
    url = (
        f"https://maps.googleapis.com/maps/api/place/details/json"
        f"?place_id={PLACE_ID}&fields=reviews&key={GOOGLE_API_KEY}"
    )
    response = requests.get(url)
    data = response.json()
    reviews = data.get("result", {}).get("reviews", [])
    return jsonify(reviews)

@app.route("/")
def home():
    return "✅ Google Reviews API is live!"

if __name__ == "__main__":
    app.run()
