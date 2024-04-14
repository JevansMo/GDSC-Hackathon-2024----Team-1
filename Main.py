# flask is a module that should allow us to connect front end with back end,
# but i'm still figuring it out -Jalen
from flask import Flask, render_template, request
from Shuttle import Shuttle
from weather import Weather

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('map.html')

@app.route('/', methods=['POST'])
def get_value():
    dst = request.form['destination']

    test = Shuttle(dst, 12, "van", 20)
    today = Weather()

    dist = 0
    if dst == 'LSU':
        dist = 2
    elif dst == 'UNO':
        dist = 6

    eta = test.eta_to_xula(dist, today.delay),
    condition = today.condition

    print(eta)
    print(condition)

    return render_template('map.html', eta=eta, condition=condition)


def main():
    pass



if __name__ == "__main__":
    # creates a webserver -Jalen
    app.run(debug=True)