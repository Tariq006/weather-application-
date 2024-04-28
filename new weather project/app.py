
from flask import Flask, render_template, request
import requests 

app = Flask(__name__) 





@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form['name']

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=f7595fd05df4d27f4ca5447e2c8929cd'
        response = requests.get(url.format(city_name)).json()
        
        temp = response['main']['temp']
        weather = response['weather'][0]['description']
        min_temp = response['main']['temp_min']
        max_temp = response['main']['temp_max']
        lon = response['coord']['lon']
        lat= response['coord']['lat']
        icon = response['weather'][0]['icon']
        
        print(temp,weather,min_temp,max_temp,lon,lat,icon)
        return render_template('index.html',temp=temp,weather=weather,min_temp=min_temp,max_temp=max_temp,lon=lon,lat=lat,icon=icon, city_name = city_name)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
