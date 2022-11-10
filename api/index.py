from flask import Flask, render_template
import requests
from threading import Thread
import pandas as pd

app = Flask(__name__)

def keep_alive(url):
    res = requests.get(url,timeout=1)
    print(url)

@app.route('/')
def hello():
    data = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTswRgT0ErnCANmfE-vjn6R5e3cRKu9lQmF1EE1V-YJ8Qu40Uq_zUcvvOJPHhnGQbnzyxI6fRLTdR9S/pub?output=csv")
    temp = list(data['URL'])
    for i in temp:
        background_thread = Thread(target=keep_alive,args=(str(i),))
        background_thread.start()
    return 'Hello, All Trigger Job Successfull'


@app.route('/test')
def test():
    return 'Test'

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)
