from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1 style='color:purple;'>Welcome to Flask</h1><p>This is your home page.</p>"

@app.route("/about")
def about():
    return "<h2>About Us</h2><p>We are learning Flask with love 💜</p>"

if __name__ == "__main__":
    app.run(debug=True)
