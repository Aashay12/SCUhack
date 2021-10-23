from flask import Flask, render_template, request, redirect, session
from flask_cors import CORS
import json
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'any'
CORS(app)

sender_email = os.getenv('SENDER_EMAIL')
password = os.getenv('PASSWORD')
receiver_email = os.getenv('RECEIVER_EMAIL')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = sender_email
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def processForm():
    if request.method == 'GET':
        # return render_template('form.html')
        pass
    else:
        # rule engine
        pass


@app.route('/result')
def result():
    pass
