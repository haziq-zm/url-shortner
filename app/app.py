from flask import Flask

app = Flask(__name__)

@app.route("/")
def health_check():
    return "URL Shortener Server is running!"

if __name__ == "__main__":
    app.run(debug=True)
