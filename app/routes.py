from flask import render_template
from app import app
from app.widgets.ip_info_client import get_ip_info
from app.widgets.metaweather import get_weather


@app.route('/')
@app.route('/index')
def index():
    ip_info = get_ip_info('151.101.65.69')
    weather = get_weather(ip_info.all['loc'])
    return render_template('index.html', title='EyeOverYou', ip=ip_info, weather=weather)


@app.route('/about')
def about():
    return render_template('about.html')
