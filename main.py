from flask import Flask, render_template,request
from requests import get

app = Flask(__name__)

def getweatherinfo(city):
    request = get(f"https://wttr.in/{city}?format=j2")
    data = request.json()

    current_info = data["current_condition"][0]
    info = data["weather"][0]

    weatherinfo = {
    "city" : city,
    "current_temperature": current_info["FeelsLikeC"],
    "average_temperature": info["avgtempC"],
    "humidity": current_info["humidity"],
    "visibility": current_info["visibility"],
    "description": current_info["weatherDesc"][0]["value"],
    "wind_speed": current_info["windspeedKmph"],
    "wind_direction": current_info["winddir16Point"],
    "observation_time": current_info["observation_time"]
}
    return weatherinfo


@app.route('/')
def form():
    return render_template('home.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    weatherinfo = getweatherinfo(name)  
    return render_template('submit.html', name=name, weatherinfo=weatherinfo)

if __name__ == '__main__':
    app.run(debug=True)