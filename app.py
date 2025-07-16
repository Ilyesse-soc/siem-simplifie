from flask import Flask, render_template
from mongo.mongo_config import get_mongo_collection

app = Flask(__name__)

@app.route("/")
def index():
    logs = get_mongo_collection().find().sort("timestamp", -1)
    return render_template("index.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
