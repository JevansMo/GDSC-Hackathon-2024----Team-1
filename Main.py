# flask is a module that should allow us to connect front end with back end,
# but i'm still figuring it out -Jalen
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Team 1 is the best!!"

def main():
    pass


if __name__ == "__main__":
    # creates a webserver -Jalen
    app.run(host="0.0.0.0", port=8000, debug=True)