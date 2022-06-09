from flask import Flask, render_template
import os

phone = os.environ.get("PHONE")
email = os.environ.get("EMAIL")
fa_kit = os.environ.get("FA_KIT")


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", phone=phone, email=email, fa_kit=fa_kit)


if __name__ == "__main__":
    app.run()

