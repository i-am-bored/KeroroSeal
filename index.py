from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("./keroro-ad09f-firebase-adminsdk-kfn8v-b85daedfc8.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://keroro-ad09f-default-rtdb.asia-southeast1.firebasedatabase.app'
})
data = db.reference()

app = Flask(__name__)

@app.route('/main')
def menu():
    return render_template('main.html')

@app.route('/bought') # 빵 개수 등록
def bought_bread():
    return render_template('bought.html')

@app.route('/registerseal') # 띠부씰 등록
def bought_bread():
    return render_template('bought.html')

@app.route('/mykeroro') # 내 빵 목록과 띠부씰 목록
def bought_bread():
    return render_template('bought.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1')