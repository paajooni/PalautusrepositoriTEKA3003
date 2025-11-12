from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    name = os.environ.get("APP_NAME", "Oma kontti")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>{name}</h1><p>Kontissa ajetaan Flask-sovellusta.<br>Palvelimen aika: {now}</p>"

if __name__ == "__main__":
    # Flaskin sisäänrakennettua kehityspalvelinta käytetään tässä yksinkertaisuuden vuoksi
    app.run(host="0.0.0.0", port=80)